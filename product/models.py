from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta: #클래스의 이름을 설정하는 클래스(메타클래스)
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu',on_delete=models.CASCADE)
    #on_delete = 부모가 지워지면 자식도 지워짐
    
    class Meta:
        db_table = 'categories'
        
class Drink(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'drinks'

class Allergy_drink(models.Model):
    allergy = models.ForeignKey('Allergy',on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink',on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'allergy_drinks'
        
class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    sodium_mg = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    saturated_fat = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    sugars_g = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    protein_g = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    caffein_mg = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    drink = models.ForeignKey("Drink",on_delete=models.CASCADE)
    size = models.ForeignKey("Size",on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'nutritions'

class Image(models.Model):
    image_url = models.TextField()
        
    class Meta:
        db_table = "images"
        
class Image_drink(models.Model):
    image = models.ForeignKey('Image',on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink',on_delete=models.CASCADE)
    
    class Meta:
        db_table = "image_drinks"

class Allergy(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = "allergies"

class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45,null=True)
    size_fluid_ounce = models.CharField(max_length=45,null=True)
    
    class Meta:
        db_table = "sizes"