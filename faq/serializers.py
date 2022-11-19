from rest_framework import serializers
from .models import FAQ, Category




class FAQSerializer(serializers.ModelSerializer):
    # author_id = serializers.CharField(
    #     source="author.id", read_only=True) 
    # category = serializers.StringRelatedField(read_only=True) 
    
    class Meta:
        model = FAQ
        # fields =(
        #     'question',
        #     'answer',
        #     'category'
        # )
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    faq = FAQSerializer(read_only=True)
    class Meta:
        model = Category
        fields = (
            'faq',
        )