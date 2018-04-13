# gripjax.py

from grip import GitHubRenderer, Grip

MATHJAX_SCRIPT = """
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS-MML_HTMLorMML-full"></script>
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" onload="javascript:MathJax.Hub.Queue(['Typeset', MathJax.Hub]);">
"""

class MathJaxRenderer(GitHubRenderer):
    def patch(self, html):
        return super(MathJaxRenderer, self).patch(html) + MATHJAX_SCRIPT

Grip(renderer=MathJaxRenderer()).run()

