# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1557259685.466429
_enable_loop = True
_template_filename = 'themes/monospace/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        date_format = context.get('date_format', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        posts = context.get('posts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        math = _mako_get_namespace(context, 'math')
        posts = context.get('posts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        date_format = context.get('date_format', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for post in posts:
            __M_writer('        <div class="postbox">\n        <h1><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('">')
            __M_writer(str(post.title()))
            __M_writer('</a></h1>\n            <div class="meta" style="background-color: rgb(234, 234, 234); ">\n                <span class="authordate">\n                    ')
            __M_writer(str(messages("Posted:")))
            __M_writer(' by <b>')
            __M_writer(str(post.author()))
            __M_writer('</b> <time class="published" datetime="')
            __M_writer(str(post.date.isoformat()))
            __M_writer('">')
            __M_writer(str(post.formatted_date(date_format)))
            __M_writer('</time>\n                </span>\n                <br>\n                <span class="tags">Tags:&nbsp;\n')
            if post.tags:
                for tag in post.tags:
                    __M_writer('                            <a class="tag" href="')
                    __M_writer(str(_link('tag', tag)))
                    __M_writer('"><span>')
                    __M_writer(str(tag))
                    __M_writer('</span></a>\n')
            __M_writer('                </span>\n            </div>\n        ')
            __M_writer(str(post.text(teaser_only=index_teasers)))
            __M_writer('\n')
            if not post.meta('nocomments'):
                __M_writer('            ')
                __M_writer(str(comments.comment_link(post.permalink(), post.base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n')
        __M_writer('    ')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n    ')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/monospace/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "35": 0, "52": 2, "53": 3, "54": 4, "55": 5, "60": 8, "65": 35, "71": 6, "79": 6, "80": 7, "81": 7, "87": 9, "101": 9, "102": 10, "103": 11, "104": 12, "105": 12, "106": 12, "107": 12, "108": 15, "109": 15, "110": 15, "111": 15, "112": 15, "113": 15, "114": 15, "115": 15, "116": 19, "117": 20, "118": 21, "119": 21, "120": 21, "121": 21, "122": 21, "123": 24, "124": 26, "125": 26, "126": 27, "127": 28, "128": 28, "129": 28, "130": 30, "131": 32, "132": 32, "133": 32, "134": 33, "135": 33, "136": 34, "137": 34, "143": 137}}
__M_END_METADATA
"""
