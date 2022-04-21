import decimal

import graphene
from graphene_django import DjangoObjectType

from .models import Category, Book, Grocery


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "title")


class Book2Type(DjangoObjectType):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "isbn",
            "pages",
            "price",
            "quantity",
            "description",
            "status",
            "date_created",
        )


class GroceryType(DjangoObjectType):
    class Meta:
        model= Grocery
        fields = (
            "product_tag",
            "name",
            "category",
            "price",
            "quantity",
            "imageurl",
            "status",
            "date_created",
        )

class Query(graphene.ObjectType):
    categories = graphene.List(GroceryType)
    books = graphene.List(Book2Type)
    groceries = graphene.List(GroceryType) 

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()

    def resolve_books(root, info, **kwargs):
        return Book.objects.all()

    def resolve_groceries(root, info, **kwargs):
        return Grocery.objects.all()


class UpdateCategory(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        id = graphene.ID()

    category = graphene.Field(CategoryType)


    @classmethod 
    def mutate(cls, root, info, title, id):
        category = Category.objects.get(pk=id)
        category.title = title 
        category.save()
        return UpdateCategory(category=category)

class CreateCategory(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root,info, title):
        category = Category()
        category.title = title
        category.save()

        return CreateCategory(category=category)

class BookInput(graphene.InputObjectType):
    title = graphene.String()
    author = graphene.String()
    pages = graphene.Int()
    price = graphene.Int()
    quantity = graphene.Int()
    description = graphene.String()
    status = graphene.String()


class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(Book2Type)

    @classmethod
    def mutate(cls, root, info, input):
        book = Book()
        book.title = input.title 
        book.author = input.author
        book.pages = input.pages
        book.price = input.price
        book.quantity = input.quantity
        book.description = input.description
        book.status = input.status
        book.save()

        return CreateBook(book=book)


class UpdateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)
        id = graphene.ID()

    book = graphene.Field(Book2Type)

    @classmethod
    def mutate(cls, root, info, input, id):
        book = Book.objects.get(pk=id)
        book.name = input.name
        book.description = input.description
        book.price = decimal.Decimal(input.price)
        book.quantity = input.quantity
        book.save()

        return UpdateBook(book=book)

class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()


# schema = graphene.Schema(query=Query)
