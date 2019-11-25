# -*- encoding: utf-8 -*-

from .support import HPyTest

class TestUnicodeObject(HPyTest):

    def test_Unicode_Check(self):
        mod = self.make_module("""
            HPy_DEF_METH_O(f)
            static HPy f_impl(HPyContext ctx, HPy self, HPy arg)
            {
                if (HPyUnicode_Check(ctx, arg))
                    return HPy_Dup(ctx, ctx->h_True);
                return HPy_Dup(ctx, ctx->h_False);
            }
            @EXPORT f HPy_METH_O
            @INIT
        """)
        assert mod.f('hello') is True
        assert mod.f(b'hello') is False

    def test_Unicode_AsUTF8String(self):
        mod = self.make_module("""
            HPy_DEF_METH_O(f)
            static HPy f_impl(HPyContext ctx, HPy self, HPy arg)
            {
                return HPyUnicode_AsUTF8String(ctx, arg);
            }
            @EXPORT f HPy_METH_O
            @INIT
        """)
        s = 'hellò'
        b = mod.f(s)
        assert type(b) is bytes
        assert b == s.encode('utf-8')