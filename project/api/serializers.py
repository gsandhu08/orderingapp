from rest_framework import serializers

from .models import Customer, MenuItems, Order, RestaurantList

class RestListSerializer(serializers.ModelSerializer):
    class Meta:
        model= RestaurantList
        fields = ['id','name']

class RestDetailSerializer_create(serializers.ModelSerializer):
    # menu_list = serializers.SerializerMethodField()
    # def get_menu_list(self,obj):
    #     return obj.menu_list
    class Meta:
        model= RestaurantList
        fields = ['id','profile_picture','name','address','owner_name','contact_person','mobile','email',
                    'opening_time','closing_time','rating','active','disable','created_date','updated_date','menu_list']

class RestDetailSerializer(serializers.ModelSerializer):
    menu_list = serializers.SerializerMethodField()
    def get_menu_list(self,obj):
        items_list=[]
        list = obj.menu_list
        if obj.menu_list:
            list= list.split(',')
        else:
            return []
        for i in list:
            try:
                items = MenuItems.objects.get(id=i)
                items_serializer = ItemsSerializer(items)
                items_list.append(items_serializer.data)
            except Exception as e:
                print(str(e))
        return items_list
        
    class Meta:
        model= RestaurantList
        fields = ['id','profile_picture','name','address','owner_name','contact_person','mobile','email',
                    'opening_time','closing_time','rating','active','disable','created_date','updated_date','menu_list']

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    list_of_items = serializers.SerializerMethodField(read_only=True)
    def get_list_of_items(self,obj):
        items_list=[]
        list = obj.list_of_items
        if obj.list_of_items:
            list= list.split(',')
        else:
            return []
        for i in list:
            try:
                items = MenuItems.objects.get(id=i)
                items_serializer = ItemsSerializer(items)
                items_list.append(items_serializer.data.get('name'))
            except Exception as e:
                print(str(e))
        return items_list

    class Meta:
        model = Order
        fields = ['id','customer_id','restaurant_id','created_time', 'updated_time','total_amount','list_of_items']

class OrderSerializer_create(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','customer_id','restaurant_id','created_time', 'updated_time','total_amount','list_of_items']