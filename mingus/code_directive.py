from cgi import escape

from docutils import nodes
from docutils.parsers.rst import directives, Directive


class CodeDirective(Directive):
    """
    reStructuredText directive to show code listings with google-code-prettify
    """

    has_content = True

    def run(self):
        self.assert_has_content()
        text = '<pre class="prettyprint">%s</pre>' % self._get_escaped_content()
        return [nodes.raw('', text, format='html')]

    def _get_escaped_content(self):
        return '\n'.join(map(escape, self.content))

directives.register_directive("code-list", CodeDirective)
directives.register_directive("sourcecode", CodeDirective)
