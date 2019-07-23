from django.test import TestCase


class BlockListViewTests(TestCase):
    databases = {'default', 'java_wallet'}

    def test_slash_redirect(self):
        response = self.client.get('/blocks')
        self.assertEqual(response.status_code, 301)

    def test_ok(self):
        response = self.client.get('/blocks/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'blocks found')
        self.assertContains(response, 'Blockchain Explorer - Blocks</title>')
        self.assertQuerysetEqual(response.context['blocks'], [])


class BlockDetailViewTests(TestCase):
    databases = {'default', 'java_wallet'}

    def test_404(self):
        response = self.client.get('/block/abc')
        self.assertEqual(response.status_code, 404)
