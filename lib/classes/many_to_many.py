class Article:
    # Class-level list to store all Article instances
    all_articles = []

    def __init__(self, author, magazine, title):
        # Validate parameters
        if not isinstance(author, Author) or not isinstance(magazine, Magazine) or not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Invalid author, magazine, or title")
        
        # Assign instance variables
        self._author = author
        self._magazine = magazine
        self._title = title
        
        # Append to the class-level all_articles list
        Article.all_articles.append(self)

        # Add this article to both the author's and the magazine's articles
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title  # Title is immutable, no setter

    @property
    def author(self):
        return self._author  # Author is immutable, no setter

    @property
    def magazine(self):
        return self._magazine  # Magazine is immutable, no setter

    @classmethod
    def all(cls):
        return cls.all_articles  # Return all instances of Article


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name  # Name is immutable

    def articles(self):
        return self._articles  # Return articles written by this author

    def magazines(self):
        # Collect unique magazines where the author has written articles
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Create and return a new article
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        # Extract unique categories (topics) from the magazines the author has written for
        topic_areas = {article.magazine.category for article in self._articles}
        return list(topic_areas) if topic_areas else None


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        
        # Initialize name and category as private variables
        self._name = name
        self._category = category
        self._articles = []
        
        # Add this magazine to the global list
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name  # Name is immutable after initialization

    @property
    def category(self):
        return self._category  # Category is immutable after initialization

    def articles(self):
        return self._articles  # Return all articles for this magazine

    def contributors(self):
        # Collect unique authors who have contributed to this magazine
        return list({article.author for article in self._articles})

    def article_titles(self):
        # Return the titles of articles written for this magazine
        return [article.title for article in self._articles] if self._articles else None

    def add_article(self, author, title):
        if not isinstance(author, Author) or not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Invalid author or title")
        
        # Create and add the article to the magazine's article list
        article = Article(author, self, title)
        self._articles.append(article)
        return article

    def contributing_authors(self):
    # Return a list of authors who have written more than one article for this magazine
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

    # Filter authors who have written more than 2 articles
        authors_with_multiple_articles = [author for author, count in author_counts.items() if count > 2]

    # Return None if no authors meet the condition, otherwise return the list
        return authors_with_multiple_articles if authors_with_multiple_articles else None