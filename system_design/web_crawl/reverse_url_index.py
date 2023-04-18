class ReverseUrlIndex:
    def __init__(self):
        self.index = {}

    def add_url(self, url):
        # Split the URL into its component directories and domains
        directories = url.split("/")[::-1]
        domains = url.split("/")[2].split(".")[::-1]
        # Create keys for all directory combinations and domain/subdomain combinations
        for i in range(len(directories)):
            key = "/".join(directories[:i+1][::-1])
            if key not in self.index:
                self.index[key] = set()
            self.index[key].add(url)
        for i in range(len(domains)):
            key = ".".join(domains[:i+1][::-1])
            if key not in self.index:
                self.index[key] = set()
            self.index[key].add(url)

    def get_urls_with_prefix(self, prefix):
        # Split the prefix into its component directories and domains
        directories = prefix.split("/")[::-1]
        domains = prefix.split("/")[2].split(".")[::-1]
        # Starting with the last directory and domain, find all URLs that match the prefix
        urls = set(self.index.get(directories[-1], [])).intersection(self.index.get(domains[-1], []))
        for i in range(1, len(directories)):
            next_urls = set(self.index.get("/".join(directories[:i+1][::-1]), [])).intersection(self.index.get(".".join(domains[:i+1][::-1]), []))
            urls = urls.intersection(next_urls)
        return urls


index = ReverseUrlIndex()

# Add some example URLs to the index
index.add_url("https://www.example.com/about")
index.add_url("https://www.example.com/blog/2021/03/01/new-post")
index.add_url("https://www.example.com/contact")
index.add_url("https://www.example.com/blog/2022/04/11/new-post")

# Search for all URLs that start with "https://www.example.com/blog"
results = index.get_urls_with_prefix("https://www.example.com/blog")
for url in results:
    print(url)