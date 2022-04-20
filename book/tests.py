import json

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer

from book.models import Book


class MyBookTestCase(GraphQLTestCase):
    GRAPHQL_URL = "/graphql"

    def setUp(self):
        self.book = mixer.blend(Book)

    def test_some_query(self):
        response = self.query(
            '''
            query {
                allBooks {
                    id 
                    title
                    yearPublished
                    author
                    review
                }
            }
            ''',
        )
        
        self.assertResponseNoErrors(response)
        
        content = json.loads(response.content)

        self.assertEqual(
            content, 
            {
                "data": {
                    "allBooks": [
                        {
                            "author": self.book.author,
                            "id": str(self.book.id),
                            "review": self.book.review,
                            "title": self.book.title,
                            "yearPublished": self.book.year_published
                        }
                    ]
                }
            }
        )

    def test_update(self):
        new_book = mixer.blend(Book)

        response = self.query(
            '''
            mutation updateBook($input: BookInput!){
                updateBook(bookData: $input) {
                    book {
                        id
                        title
                        review
                        author
                        yearPublished
                    }
                }
            }
            ''',
            variables={
                "input": {
                    "id": self.book.id,
                    "title": new_book.title,
                    "review": new_book.review,
                    "author": new_book.author,
                    "yearPublished": new_book.year_published
                }
            },
            # op_name="updateBook"
        )
        
        self.assertResponseNoErrors(response)
        
        content = json.loads(response.content)
        self.assertEqual(
            content, 
            {
                "data": {
                    "updateBook": {
                        "book": {
                            "id": str(self.book.id),
                            "title": new_book.title,
                            "review": new_book.review,
                            "author": new_book.author,
                            "yearPublished": new_book.year_published
                        }
                    }
                }
                
            }
        )

    def test_create(self):
        new_book = mixer.blend(Book)
        
        response = self.query(
            '''
            mutation createBook($input: BookInput!){
                createBook(bookData: $input) {
                    book {
                        id
                        title
                        review
                        author
                        yearPublished
                    }
                }
            }
            ''',
            variables={
                "input": {
                    "title": new_book.title,
                    "review": new_book.review,
                    "author": new_book.author,
                    "yearPublished": new_book.year_published
                }
            },
            # op_name="updateBook"
        )
        
        self.assertResponseNoErrors(response)
        
        content = json.loads(response.content)
        content["data"]["createBook"]["book"].pop("id")
        self.assertEqual(
            content, 
            {
                "data": {
                    "createBook": {
                        "book": {
                            "title": new_book.title,
                            "review": new_book.review,
                            "author": new_book.author,
                            "yearPublished": new_book.year_published
                        }
                    }
                }
                
            }
        )

    def test_delete(self):
        new_book = mixer.blend(Book)
        
        response = self.query(
            '''
            mutation deleteBook($id: ID!){
                deleteBook(id: $id) {
                    book {
                        id
                        title
                        review
                        author
                        yearPublished
                    }
                }
            }
            ''',
            variables={
                "id": new_book.id
            },
            # op_name="updateBook"
        )
        
        self.assertResponseNoErrors(response)
        
        content = json.loads(response.content)
        self.assertEqual(
            content, 
            {'data': {'deleteBook': None}}
        )


    def test_with_variables(self):
        response = self.query(
            '''
            query book($id: ID){
                book(bookId: $id) {
                    id
                    title
                    review
                    author
                    yearPublished
                }
            }
            ''',
            variables={"id": self.book.id}
        )

        self.assertResponseNoErrors(response)
        
        content = json.loads(response.content)

        self.assertEqual(
            content, 
            {
                "data": {
                    "book": {
                        "author": self.book.author,
                        "id": str(self.book.id),
                        "review": self.book.review,
                        "title": self.book.title,
                        "yearPublished": self.book.year_published
                    }
                }
            }
        )