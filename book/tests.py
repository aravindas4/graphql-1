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
            op_name="book",
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