# Copyright (c) 2015, Nginx Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of the Nginx Inc.

import re

from docutils.nodes import emphasis,reference,Text
from docutils.parsers.rst.roles import set_classes

def icon_role(role, rawtext, text, lineno, inliner, options={}, content=[]):

    options.update({'classes': ["fa"]+["fa-" + x for x in text.split(",")]})
    options['classes'].append('icon-holder')
    set_classes(options)
    node = emphasis(**options)
    return [node], []

def github_role(role, rawtext, text, lineno, inliner, options={}, content=[]):

    font_options = {'classes': ["fa", "fa-github"]}
    set_classes(options)
    node = reference(rawtext, text, refuri="https://github.com/"+text, **options)
    set_classes(font_options)
    node.insert(0, emphasis(**font_options))
    node.insert(1, Text(u"\u00A0"))

    return [node], []

def bitbucket_role(role, rawtext, text, lineno, inliner, options={}, content=[]):

    font_options = {'classes': ["fa", "fa-bitbucket"]}
    set_classes(options)
    node = reference(rawtext, text, refuri="https://bitbucket.org/"+text, **options)
    set_classes(font_options)
    node.insert(0, emphasis(**font_options))
    node.insert(1, Text(u"\u00A0"))

    return [node], []

def setup(app): # pragma: no cover
    app.info('Adding the font awesome icon role')
    app.add_role('icon', icon_role)
    app.info('Adding the font awesome github role')
    app.add_role('github', github_role)
    app.info('Adding the font awesome bitbucket role')
    app.add_role('bitbucket', github_role)

    return
