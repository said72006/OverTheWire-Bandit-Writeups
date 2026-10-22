import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class DocumentationTests(unittest.TestCase):
    def test_readme_level_links_exist(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        links = re.findall(r"\]\((levels/Level-\d+\.md)\)", readme)
        self.assertGreaterEqual(len(links), 20)
        for link in links:
            with self.subTest(link=link):
                self.assertTrue((ROOT / link).is_file(), link)

    def test_no_private_key_blocks_in_markdown(self):
        for file in ROOT.rglob("*.md"):
            with self.subTest(file=str(file.relative_to(ROOT))):
                text = file.read_text(encoding="utf-8")
                self.assertNotIn("-----BEGIN OPENSSH PRIVATE KEY-----", text)
                self.assertNotIn("-----BEGIN RSA PRIVATE KEY-----", text)

    def test_levels_named_consistently(self):
        levels = sorted((ROOT / "levels").glob("Level-*.md"))
        numbers = [int(path.stem.split("-")[1]) for path in levels]
        self.assertEqual(numbers, list(range(max(numbers) + 1)))


if __name__ == "__main__":
    unittest.main()
