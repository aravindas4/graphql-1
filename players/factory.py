import factory.fuzzy
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "auth.User"
        django_get_or_create = ("username",)

    email = factory.Faker("ascii_safe_email")
    username = factory.lazy_attribute(lambda obj: f"{obj.email}")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class PlayerBoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "players.PlayerBoard"

    points = factory.fuzzy.FuzzyInteger(0)


class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "players.Player"

    user = factory.SubFactory(UserFactory)
    board = factory.SubFactory(PlayerBoardFactory)
    picture = factory.Faker("file_path")
    gender = factory.fuzzy.FuzzyChoice(["MALE", "FEMALE", "THIRD"])
    motto = factory.Faker("paragraph")
