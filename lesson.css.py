from bs4 import BeautifulSoup

html = """
<body>
    <h1>タイトル</h1>
    <h2>演習内容</h2>
    <ol id="step1" class="study-list">
        <li>Python基礎</li>
        <li id="target">THML基礎</li>
        <li>JS基礎</li>
        <li>Pythonライブラリの基礎</li>
    </ol>
</body>
"""

soup = BeautifulSoup(html, "lxml")

#print(soup.find_all(class_="study-list"))
print(soup.select('li:-soup-contains("Python")'))