from rest_framework.serializers import ModelSerializer, SerializerMethodField
from products.models import Product, EditableProduct

from images.models import Image
from product_details.serializers import SizeAndQuantitySerializer, ProductDetailSerializer
from review_rating_qna.serializers import ReviewSerializer, Q_N_ASerializer
from images.serializers import ImageSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


# serializer to get multiple products


class ProductSerializer(ModelSerializer):
    size_n_quantity = SizeAndQuantitySerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'product_type', 'product_color', 'product_design_type', 'search_kw',  'original_price', 'seller_discount',
                  'image', 'rating', 'time_stamp', 'deleted', 'size_n_quantity']

# same as above but it loads more data and is used to get only one product and its detail


class SingleProductSerializer(ModelSerializer):
    size_n_quantity = SizeAndQuantitySerializer(many=True)
    product_details = ProductDetailSerializer(many=True)
    reviews = SerializerMethodField()
    q_n_as = SerializerMethodField()
    product_images = SerializerMethodField()
    # item_in_cart = SerializerMethodField()
    item_in_wishlist = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'product_type', 'product_color', 'product_design_type', 'search_kw',  'original_price', 'seller_discount',
                  'image', 'rating', 'description', 'time_stamp', 'deleted', 'size_n_quantity', 'product_details', 'reviews', 'q_n_as', 'product_images',  'item_in_wishlist']  # 'item_in_cart',

    def get_reviews(self, obj):
        p_reviews = obj.reviews.all()[:3]
        return ReviewSerializer(instance=p_reviews, many=True).data

    def get_q_n_as(self, obj):
        p_q_n_as = obj.q_n_as.all()[:3]
        return Q_N_ASerializer(instance=p_q_n_as, many=True).data

    def get_product_images(self, obj):
        images = obj.product_images.all().order_by('position')
        return ImageSerializer(instance=images, many=True).data

    # def get_item_in_cart(self, obj):
    #     if (not self.context['is_anonymous']):
    #         if obj.cart_items.filter(current_user=self.context["user"]).exists():
    #             return True
    #     return False

    def get_item_in_wishlist(self, obj):
        if (not self.context['is_anonymous']):
            if obj.wishlist_items.filter(current_user=self.context["user"]).exists():
                return obj.wishlist_items.values('id').get(current_user=self.context["user"])
        return False
     # same as above but it loads more reviews and few details about the product


class ProductReviewSerializer(ModelSerializer):
    reviews = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name',  'original_price', 'seller_discount',
                  'image', 'rating', 'reviews']

    def get_reviews(self, obj):
        p_reviews = obj.reviews.all().order_by('-rating')
        return ReviewSerializer(instance=p_reviews, many=True).data

# same as above but it loads more questions and answers and few details about the product


class ProductQnaSerializer(ModelSerializer):
    q_n_as = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name',  'original_price', 'seller_discount',
                  'image', 'rating', 'q_n_as']

    def get_q_n_as(self, obj):
        p_q_n_as = obj.q_n_as.all()
        return Q_N_ASerializer(instance=p_q_n_as, many=True).data


class NormalProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'original_price',
                  'seller_discount', 'image', 'rating']


class EditableProductSerializer(ModelSerializer):
    class Meta:
        model = EditableProduct
        fields = '__all__'
