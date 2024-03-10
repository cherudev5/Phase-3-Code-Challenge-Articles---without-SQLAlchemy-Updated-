# Author class
class Author:
    def __init__(self, name):
        # Validate and set the author's name
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Create and associate a new article with the author and magazine
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        # Return unique categories of magazines the author has contributed to
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


# Magazine class
class Magazine:
    def __init__(self, name, category):
        # Validate and set the magazine's name and category
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) <= 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        # Return unique authors who have written for the magazine
        return list(set(article.author for article in self._articles if article.author))

    def article_titles(self):
        # Return titles of all articles written for the magazine
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        # Return authors who have written more than 2 articles for the magazine
        authors_count = {}
        for article in self._articles:
            author = article.author
            if author:
                authors_count[author] = authors_count.get(author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2]


# Article class
class Article:
    def __init__(self, author, magazine, title):
        # Validate and set the article's title, author, and magazine
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Article title must be a string between 5 and 50 characters.")
        self._title = title
        self._author = author
        self._magazine = magazine

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    def __setattr__(self, name, value):
        # Prevent modification of attributes after instantiation
        if hasattr(self, name):
            raise AttributeError("Cannot modify attribute after instantiation.")
        super().__setattr__(name, value)
