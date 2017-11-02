__all__ = ['solve']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['OPS', 'solve_numbers', 'abs', 'solve_letters', 'bestvalsums', '_recurse_solve_letters', '_solve_numbers', 'OPCOST', 'fullsize', '_recurse_solve_numbers', 'word_in_dictionary', 'bestdiff', 'stringify_result', 'serialise_result', 'tidyup_result', 'sufficient_letters'])
@Js
def PyJsHoisted__recurse_solve_letters_(letters, node, used_letter, cb, answer, this, arguments, var=var):
    var = Scope({'letters':letters, 'node':node, 'used_letter':used_letter, 'cb':cb, 'answer':answer, 'this':this, 'arguments':arguments}, var)
    var.registers(['node', 'i', 'used_letter', 'letters', 'done', 'cb', 'c', 'answer'])
    if var.get('node').get('0'):
        var.get('cb')(var.get('answer'), var.get('node').get('0'))
    if (var.get('answer').get('length')==var.get('letters').get('length')):
        return var.get('undefined')
    PyJs_Object_0_ = Js({})
    var.put('done', PyJs_Object_0_)
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('letters').get('length')):
        try:
            var.put('c', var.get('letters').callprop('charAt', var.get('i')))
            if (var.get('used_letter').get(var.get('i')) or var.get('done').get(var.get('c'))):
                continue
            if var.get('node').get(var.get('c')):
                var.get('used_letter').put(var.get('i'), Js(True))
                var.get('done').put(var.get('c'), Js(True))
                var.get('_recurse_solve_letters')(var.get('letters'), var.get('node').get(var.get('c')), var.get('used_letter'), var.get('cb'), (var.get('answer')+var.get('c')))
                var.get('used_letter').put(var.get('i'), Js(False))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted__recurse_solve_letters_.func_name = '_recurse_solve_letters'
var.put('_recurse_solve_letters', PyJsHoisted__recurse_solve_letters_)
@Js
def PyJsHoisted_solve_letters_(letters, cb, this, arguments, var=var):
    var = Scope({'letters':letters, 'cb':cb, 'this':this, 'arguments':arguments}, var)
    var.registers(['cb', 'letters'])
    PyJs_Object_1_ = Js({})
    var.get('_recurse_solve_letters')(var.get('letters'), var.get('dictionary'), PyJs_Object_1_, var.get('cb'), Js(''))
PyJsHoisted_solve_letters_.func_name = 'solve_letters'
var.put('solve_letters', PyJsHoisted_solve_letters_)
@Js
def PyJsHoisted_sufficient_letters_(word, letters, this, arguments, var=var):
    var = Scope({'word':word, 'letters':letters, 'this':this, 'arguments':arguments}, var)
    var.registers(['count', 'word', 'i', 'letters'])
    PyJs_Object_2_ = Js({})
    var.put('count', PyJs_Object_2_)
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('letters').get('length')):
        try:
            if var.get('count').get(var.get('letters').callprop('charAt', var.get('i'))).neg():
                var.get('count').put(var.get('letters').callprop('charAt', var.get('i')), Js(0.0))
            (var.get('count').put(var.get('letters').callprop('charAt', var.get('i')),Js(var.get('count').get(var.get('letters').callprop('charAt', var.get('i'))).to_number())+Js(1))-Js(1))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('word').get('length')):
        try:
            if var.get('count').get(var.get('word').callprop('charAt', var.get('i'))).neg():
                return Js(False)
            (var.get('count').put(var.get('word').callprop('charAt', var.get('i')),Js(var.get('count').get(var.get('word').callprop('charAt', var.get('i'))).to_number())-Js(1))+Js(1))
            if (var.get('count').get(var.get('word').callprop('charAt', var.get('i')))<Js(0.0)):
                return Js(False)
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return Js(True)
PyJsHoisted_sufficient_letters_.func_name = 'sufficient_letters'
var.put('sufficient_letters', PyJsHoisted_sufficient_letters_)
@Js
def PyJsHoisted_word_in_dictionary_(word, this, arguments, var=var):
    var = Scope({'word':word, 'this':this, 'arguments':arguments}, var)
    var.registers(['node', 'word', 'idx'])
    var.put('node', var.get('dictionary'))
    var.put('idx', Js(0.0))
    while (var.get('idx')<var.get('word').get('length')):
        var.put('node', var.get('node').get(var.get('word').callprop('charAt', var.get('idx'))))
        (var.put('idx',Js(var.get('idx').to_number())+Js(1))-Js(1))
        if var.get('node').neg():
            return Js(False)
    if var.get('node').get('0').neg():
        return Js(False)
    return Js(True)
PyJsHoisted_word_in_dictionary_.func_name = 'word_in_dictionary'
var.put('word_in_dictionary', PyJsHoisted_word_in_dictionary_)
@Js
def PyJsHoisted__recurse_solve_numbers_(numbers, searchedi, was_generated, target, levels, valsums, trickshot, this, arguments, var=var):
    var = Scope({'numbers':numbers, 'searchedi':searchedi, 'was_generated':was_generated, 'target':target, 'levels':levels, 'valsums':valsums, 'trickshot':trickshot, 'this':this, 'arguments':arguments}, var)
    var.registers(['nj', 'i', 'was_generated', 'numbers', 'target', 'levels', 'op_cost', 'newvalsums', 'valsums', 'r', 'old_was_gen', 'fn', 'searchedi', 'ni', 'o', 'j', 'trickshot'])
    (var.put('levels',Js(var.get('levels').to_number())-Js(1))+Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('numbers').get('length')-Js(1.0))):
        try:
            var.put('ni', var.get('numbers').get(var.get('i')))
            if PyJsStrictEq(var.get('ni'),Js(False)):
                continue
            var.get('numbers').put(var.get('i'), Js(False))
            #for JS loop
            var.put('j', (var.get('i')+Js(1.0)))
            while (var.get('j')<var.get('numbers').get('length')):
                try:
                    var.put('nj', var.get('numbers').get(var.get('j')))
                    if PyJsStrictEq(var.get('nj'),Js(False)):
                        continue
                    if (((var.get('i')<var.get('searchedi')) and var.get('was_generated').get(var.get('i')).neg()) and var.get('was_generated').get(var.get('j')).neg()):
                        continue
                    for PyJsTemp in var.get('OPS'):
                        var.put('o', PyJsTemp)
                        var.put('fn', var.get('OPS').get(var.get('o')))
                        var.put('r', var.get('fn')(var.get('ni').get('0'), var.get('nj').get('0')))
                        if PyJsStrictEq(var.get('r'),Js(False)):
                            continue
                        var.put('op_cost', var.get('abs')(var.get('r')))
                        while (((var.get('op_cost')%Js(10.0))==Js(0.0)) and (var.get('op_cost')!=Js(0.0))):
                            var.put('op_cost', Js(10.0), '/')
                        if (((var.get('ni').get('0')==Js(10.0)) or (var.get('nj').get('0')==Js(10.0))) and (var.get('o')==Js('*'))):
                            var.put('op_cost', Js(1.0))
                        var.put('op_cost', var.get('OPCOST').get(var.get('o')), '*')
                        var.put('newvalsums', (var.get('valsums')+var.get('op_cost')))
                        if ((var.get('abs')((var.get('r')-var.get('target')))<var.get('abs')((var.get('bestresult').get('0')-var.get('target')))) or ((var.get('abs')((var.get('r')-var.get('target')))==var.get('abs')((var.get('bestresult').get('0')-var.get('target')))) and (var.get('trickshot') or (var.get('newvalsums')<var.get('bestvalsums'))))):
                            var.put('bestresult', Js([var.get('r'), var.get('o'), var.get('ni'), var.get('nj')]))
                            var.put('bestvalsums', var.get('newvalsums'))
                        var.get('numbers').put(var.get('j'), Js([var.get('r'), var.get('o'), var.get('ni'), var.get('nj')]))
                        var.put('old_was_gen', var.get('was_generated').get(var.get('j')))
                        var.get('was_generated').put(var.get('j'), Js(True))
                        if ((var.get('levels')>Js(0.0)) and ((var.get('trickshot') or (var.get('bestresult').get('0')!=var.get('target'))) or (var.get('newvalsums')<var.get('bestvalsums')))):
                            var.get('_recurse_solve_numbers')(var.get('numbers'), (var.get('i')+Js(1.0)), var.get('was_generated'), var.get('target'), var.get('levels'), var.get('newvalsums'), var.get('trickshot'))
                        var.get('was_generated').put(var.get('j'), var.get('old_was_gen'))
                        var.get('numbers').put(var.get('j'), var.get('nj'))
                finally:
                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            var.get('numbers').put(var.get('i'), var.get('ni'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted__recurse_solve_numbers_.func_name = '_recurse_solve_numbers'
var.put('_recurse_solve_numbers', PyJsHoisted__recurse_solve_numbers_)
@Js
def PyJsHoisted_tidyup_result_(result, this, arguments, var=var):
    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
    var.registers(['mapping', 'i', 'result', 'j', 'child', 'swappable'])
    PyJs_Object_11_ = Js({'?':Js('/'),'_':Js('-')})
    var.put('mapping', PyJs_Object_11_)
    PyJs_Object_12_ = Js({'*':Js(True),'+':Js(True)})
    var.put('swappable', PyJs_Object_12_)
    if (var.get('result').get('length')<Js(4.0)):
        return var.get('result')
    #for JS loop
    var.put('i', Js(2.0))
    while (var.get('i')<var.get('result').get('length')):
        try:
            var.put('child', var.get('result').get(var.get('i')))
            var.put('child', var.get('tidyup_result')(var.get('child')))
            if ((var.get('child').get('1')==var.get('result').get('1')) and var.get('swappable').get(var.get('result').get('1'))):
                var.get('result').callprop('splice', (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1)), Js(1.0))
                var.put('result', var.get('result').callprop('concat', var.get('child').callprop('slice', Js(2.0))))
            else:
                var.get('result').put(var.get('i'), var.get('child'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if var.get('mapping').contains(var.get('result').get('1')):
        var.get('result').put('1', var.get('mapping').get(var.get('result').get('1')))
        var.put('j', var.get('result').get('2'))
        var.get('result').put('2', var.get('result').get('3'))
        var.get('result').put('3', var.get('j'))
    else:
        if var.get('swappable').get(var.get('result').get('1')):
            @Js
            def PyJs_anonymous_13_(a, b, this, arguments, var=var):
                var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
                var.registers(['a', 'b'])
                return (var.get('b').get('0')-var.get('a').get('0'))
            PyJs_anonymous_13_._set_name('anonymous')
            var.put('childs', var.get('result').callprop('slice', Js(2.0)).callprop('sort', PyJs_anonymous_13_))
            #for JS loop
            var.put('i', Js(2.0))
            while (var.get('i')<var.get('result').get('length')):
                try:
                    var.get('result').put(var.get('i'), var.get('childs').get((var.get('i')-Js(2.0))))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('result')
PyJsHoisted_tidyup_result_.func_name = 'tidyup_result'
var.put('tidyup_result', PyJsHoisted_tidyup_result_)
@Js
def PyJsHoisted_fullsize_(array, this, arguments, var=var):
    var = Scope({'array':array, 'this':this, 'arguments':arguments}, var)
    var.registers(['array', 'i', 'l'])
    if (var.get('array').get('constructor')!=var.get('Array')):
        return Js(0.0)
    var.put('l', Js(0.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('array').get('length')):
        try:
            var.put('l', var.get('fullsize')(var.get('array').get(var.get('i'))), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return (var.get('l')+var.get('array').get('length'))
PyJsHoisted_fullsize_.func_name = 'fullsize'
var.put('fullsize', PyJsHoisted_fullsize_)
@Js
def PyJsHoisted_serialise_result_(result, this, arguments, var=var):
    var = Scope({'result':result, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'childparts', 'parts', 'thispart', 'result', 'sliced', 'child'])
    var.put('childparts', Js([]))
    #for JS loop
    var.put('i', Js(2.0))
    while (var.get('i')<var.get('result').get('length')):
        try:
            var.put('child', var.get('result').get(var.get('i')))
            if (var.get('child').get('length')>=Js(4.0)):
                var.get('childparts').callprop('push', var.get('serialise_result')(var.get('child')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    @Js
    def PyJs_anonymous_14_(a, b, this, arguments, var=var):
        var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'b'])
        return (var.get('fullsize')(var.get('b'))-var.get('fullsize')(var.get('a')))
    PyJs_anonymous_14_._set_name('anonymous')
    var.put('childparts', var.get('childparts').callprop('sort', PyJs_anonymous_14_))
    var.put('parts', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('childparts').get('length')):
        try:
            var.put('parts', var.get('parts').callprop('concat', var.get('childparts').get(var.get('i'))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    @Js
    def PyJs_anonymous_15_(l, this, arguments, var=var):
        var = Scope({'l':l, 'this':this, 'arguments':arguments}, var)
        var.registers(['l'])
        return var.get('l').get('0')
    PyJs_anonymous_15_._set_name('anonymous')
    var.put('sliced', var.get('result').callprop('slice', Js(2.0)).callprop('map', PyJs_anonymous_15_))
    var.put('thispart', Js([var.get('result').get('0'), var.get('result').get('1')]).callprop('concat', var.get('sliced')))
    return var.get('parts').callprop('concat', Js([var.get('thispart')]))
PyJsHoisted_serialise_result_.func_name = 'serialise_result'
var.put('serialise_result', PyJsHoisted_serialise_result_)
@Js
def PyJsHoisted_stringify_result_(serialised, target, this, arguments, var=var):
    var = Scope({'serialised':serialised, 'target':target, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'target', 'serialised', 'args', 'x', 'output', 'result'])
    var.put('output', Js(''))
    var.put('serialised', var.get('serialised').callprop('slice', Js(0.0)))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('serialised').get('length')):
        try:
            var.put('x', var.get('serialised').get(var.get('i')))
            var.put('args', var.get('x').callprop('slice', Js(2.0)))
            var.put('output', (((var.get('args').callprop('join', ((Js(' ')+var.get('x').get('1'))+Js(' ')))+Js(' = '))+var.get('x').get('0'))+Js('\n')), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('result', var.get('serialised').get((var.get('serialised').get('length')-Js(1.0))).get('0'))
    return Js([var.get('output'), var.get('result')])
PyJsHoisted_stringify_result_.func_name = 'stringify_result'
var.put('stringify_result', PyJsHoisted_stringify_result_)
@Js
def PyJsHoisted__solve_numbers_(numbers, target, trickshot, this, arguments, var=var):
    var = Scope({'numbers':numbers, 'target':target, 'trickshot':trickshot, 'this':this, 'arguments':arguments}, var)
    var.registers(['was_generated', 'i', 'target', 'numbers', 'trickshot'])
    @Js
    def PyJs_anonymous_16_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x'])
        return Js([var.get('x'), Js(False)])
    PyJs_anonymous_16_._set_name('anonymous')
    var.put('numbers', var.get('numbers').callprop('map', PyJs_anonymous_16_))
    var.put('was_generated', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('numbers').get('length')):
        try:
            var.get('was_generated').callprop('push', Js(False))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('bestresult', Js([Js(0.0), Js(0.0)]))
    var.get('_recurse_solve_numbers')(var.get('numbers'), Js(0.0), var.get('was_generated'), var.get('target'), var.get('numbers').get('length'), Js(0.0), var.get('trickshot'))
    return var.get('bestresult')
PyJsHoisted__solve_numbers_.func_name = '_solve_numbers'
var.put('_solve_numbers', PyJsHoisted__solve_numbers_)
@Js
def PyJsHoisted_solve_numbers_(numbers, target, trickshot, this, arguments, var=var):
    var = Scope({'numbers':numbers, 'target':target, 'trickshot':trickshot, 'this':this, 'arguments':arguments}, var)
    var.registers(['numbers', 'trickshot', 'i', 'target'])
    var.get('numbers').callprop('sort')
    var.put('bestresult', Js([var.get('numbers').get('0'), var.get('numbers').get('0')]))
    if var.get('trickshot').neg():
        #for JS loop
        var.put('i', Js(1.0))
        while (var.get('i')<var.get('numbers').get('length')):
            try:
                if (var.get('abs')((var.get('numbers').get(var.get('i'))-var.get('target')))<var.get('abs')((var.get('bestresult').get('0')-var.get('target')))):
                    var.put('bestresult', Js([var.get('numbers').get(var.get('i')), var.get('numbers').get(var.get('i'))]))
                    var.put('bestvalsums', var.get('numbers').get(var.get('i')))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        if (var.get('bestresult').get('0')==var.get('target')):
            return ((var.get('target')+Js(' = '))+var.get('target'))
    return var.get('stringify_result')(var.get('serialise_result')(var.get('tidyup_result')(var.get('_solve_numbers')(var.get('numbers'), var.get('target'), var.get('trickshot')))), var.get('target'))
PyJsHoisted_solve_numbers_.func_name = 'solve_numbers'
var.put('solve_numbers', PyJsHoisted_solve_numbers_)
var.put('abs', var.get('Math').get('abs'))
pass
pass
pass
pass
pass
pass
@Js
def PyJs_anonymous_4_(n1, n2, this, arguments, var=var):
    var = Scope({'n1':n1, 'n2':n2, 'this':this, 'arguments':arguments}, var)
    var.registers(['n1', 'n2'])
    if ((var.get('n1')<Js(0.0)) or (var.get('n2')<Js(0.0))):
        return Js(False)
    return (var.get('n1')+var.get('n2'))
PyJs_anonymous_4_._set_name('anonymous')
@Js
def PyJs_anonymous_5_(n1, n2, this, arguments, var=var):
    var = Scope({'n1':n1, 'n2':n2, 'this':this, 'arguments':arguments}, var)
    var.registers(['n1', 'n2'])
    if (var.get('n2')>=var.get('n1')):
        return Js(False)
    return (var.get('n1')-var.get('n2'))
PyJs_anonymous_5_._set_name('anonymous')
@Js
def PyJs_anonymous_6_(n2, n1, this, arguments, var=var):
    var = Scope({'n2':n2, 'n1':n1, 'this':this, 'arguments':arguments}, var)
    var.registers(['n1', 'n2'])
    if (var.get('n2')>=var.get('n1')):
        return Js(False)
    return (var.get('n1')-var.get('n2'))
PyJs_anonymous_6_._set_name('anonymous')
@Js
def PyJs_anonymous_7_(n1, n2, this, arguments, var=var):
    var = Scope({'n1':n1, 'n2':n2, 'this':this, 'arguments':arguments}, var)
    var.registers(['n1', 'n2'])
    return (var.get('n1')*var.get('n2'))
PyJs_anonymous_7_._set_name('anonymous')
@Js
def PyJs_anonymous_8_(n1, n2, this, arguments, var=var):
    var = Scope({'n1':n1, 'n2':n2, 'this':this, 'arguments':arguments}, var)
    var.registers(['n1', 'n2'])
    if ((var.get('n2')==Js(0.0)) or ((var.get('n1')%var.get('n2'))!=Js(0.0))):
        return Js(False)
    return (var.get('n1')/var.get('n2'))
PyJs_anonymous_8_._set_name('anonymous')
@Js
def PyJs_anonymous_9_(n2, n1, this, arguments, var=var):
    var = Scope({'n2':n2, 'n1':n1, 'this':this, 'arguments':arguments}, var)
    var.registers(['n1', 'n2'])
    if ((var.get('n2')==Js(0.0)) or ((var.get('n1')%var.get('n2'))!=Js(0.0))):
        return Js(False)
    return (var.get('n1')/var.get('n2'))
PyJs_anonymous_9_._set_name('anonymous')
PyJs_Object_3_ = Js({'+':PyJs_anonymous_4_,'-':PyJs_anonymous_5_,'_':PyJs_anonymous_6_,'*':PyJs_anonymous_7_,'/':PyJs_anonymous_8_,'?':PyJs_anonymous_9_})
var.put('OPS', PyJs_Object_3_)
PyJs_Object_10_ = Js({'+':Js(1.0),'-':Js(1.05),'_':Js(1.05),'*':Js(1.2),'/':Js(1.3),'?':Js(1.3)})
var.put('OPCOST', PyJs_Object_10_)
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
solve = var.to_python()