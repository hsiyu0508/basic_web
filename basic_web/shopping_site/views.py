from django.db.models import Count, Q
from django.http import Http404, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from shopping_site.models import Product
from shopping_site.serializers import ProductSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.

class AllProductView(APIView):
    @swagger_auto_schema(
        operation_summary='查詢所有產品',
        operation_description='查詢所有產品',
    )
    def get(self, request):
        products = Product.objects.filter(status=True)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)    
    @swagger_auto_schema(
        operation_summary='新增產品',
        operation_description='新增產品',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='產品名稱'
                ),
                'price': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='價錢'
                ),
                'status': openapi.Schema(
                    type=openapi.TYPE_BOOLEAN,
                    description='啟用狀態 0關 1開'
                )
            }
        )
    )
    def post(self, request, format=None):

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # @swagger_auto_schema(
    #     operation_summary='修改產品',
    #     operation_description='修改產品',
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         properties={
    #             'name': openapi.Schema(
    #                 type=openapi.TYPE_STRING,
    #                 description='產品名稱'
    #             ),
    #             'price': openapi.Schema(
    #                 type=openapi.TYPE_INTEGER,
    #                 description='價錢'
    #             ),
    #             # 'status': openapi.Schema(
    #             #     type=openapi.TYPE_INTEGER,
    #             #     description='啟用狀態 0關 1開'
    #             # )
    #         }
    #     ),
    # )
    # def put(self, request, format=None):
    #     product = self.request.query_params.get('name')
    #     print(product)
    #     product = Product.objects.filter(name=product)
    #     serializer = ProductSerializer(product,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):

    def get_object(self, product_name):
        try:
            return Product.objects.get(name=product_name,status=True)
        except Product.DoesNotExist:
            raise Http404
        
    @swagger_auto_schema(
        operation_summary='查詢產品',
        operation_description='查詢產品',
    )
    def get(self, request, product_name, format=None):
        product = self.get_object(product_name)
        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # @swagger_auto_schema(
    #     operation_summary='新增產品',
    #     operation_description='新增產品',
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         properties={
    #             'name': openapi.Schema(
    #                 type=openapi.TYPE_STRING,
    #                 description='產品名稱'
    #             ),
    #             'price': openapi.Schema(
    #                 type=openapi.TYPE_INTEGER,
    #                 description='價錢'
    #             ),
    #             'status': openapi.Schema(
    #                 type=openapi.TYPE_INTEGER,
    #                 description='啟用狀態 0關 1開'
    #             )
    #         }
    #     )
    # )
    # def post(self, request, format=None):

    #     serializer = ProductSerializer(data=request.data)

    #     if serializer.is_valid():
    #         print(serializer)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # @swagger_auto_schema(
    #     operation_summary='修改產品',
    #     operation_description='修改產品',
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         properties={
    #             'name': openapi.Schema(
    #                 type=openapi.TYPE_STRING,
    #                 description='產品名稱'
    #             ),
    #             'price': openapi.Schema(
    #                 type=openapi.TYPE_INTEGER,
    #                 description='價錢'
    #             ),
    #             'status': openapi.Schema(
    #                 type=openapi.TYPE_INTEGER,
    #                 description='啟用狀態 0關 1開'
    #             )
    #         }
    #     )
    # )
    # def put(self, request, format=None):

    #     product = Product.objects.filter(status="1")
    #     serializer = ProductSerializer(product,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        operation_summary='刪除產品',
        operation_description='刪除產品',
    )    
    def delete(self, request, product_name, format=None):
        product = self.get_object(product_name)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)