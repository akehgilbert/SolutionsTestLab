from pathlib import Path

replacements = {
    "de": [
        ('msgid "QA planning meeting"\nmsgstr ""',
         'msgid "QA planning meeting"\nmsgstr "QA-Planungsbesprechung"'),

        ('msgid "Quality Through Collaboration"\nmsgstr ""',
         'msgid "Quality Through Collaboration"\nmsgstr "Qualität durch Zusammenarbeit"'),

        ('''msgid ""
"Successful software quality is built through strong collaboration between "
"testers, developers, business stakeholders, and project managers. At "
"SolutionsTestLab, we help organizations create structured testing processes "
"that improve communication, reduce risks, and deliver reliable software "
"products."
msgstr ""''',
         '''msgid ""
"Successful software quality is built through strong collaboration between "
"testers, developers, business stakeholders, and project managers. At "
"SolutionsTestLab, we help organizations create structured testing processes "
"that improve communication, reduce risks, and deliver reliable software "
"products."
msgstr ""
"Erfolgreiche Softwarequalität entsteht durch eine enge Zusammenarbeit "
"zwischen Testern, Entwicklern, Fachbereichen und Projektmanagern. Bei "
"SolutionsTestLab unterstützen wir Unternehmen dabei, strukturierte "
"Testprozesse aufzubauen, die die Kommunikation verbessern, Risiken "
"reduzieren und zuverlässige Softwareprodukte liefern."'''),
    ],

    "fr": [
        ('msgid "QA planning meeting"\nmsgstr ""',
         'msgid "QA planning meeting"\nmsgstr "Réunion de planification QA"'),

        ('msgid "Quality Through Collaboration"\nmsgstr ""',
         'msgid "Quality Through Collaboration"\nmsgstr "La qualité grâce à la collaboration"'),

        ('''msgid ""
"Successful software quality is built through strong collaboration between "
"testers, developers, business stakeholders, and project managers. At "
"SolutionsTestLab, we help organizations create structured testing processes "
"that improve communication, reduce risks, and deliver reliable software "
"products."
msgstr ""''',
         '''msgid ""
"Successful software quality is built through strong collaboration between "
"testers, developers, business stakeholders, and project managers. At "
"SolutionsTestLab, we help organizations create structured testing processes "
"that improve communication, reduce risks, and deliver reliable software "
"products."
msgstr ""
"La qualité logicielle réussie repose sur une collaboration étroite entre "
"les testeurs, les développeurs, les parties prenantes métier et les chefs "
"de projet. Chez SolutionsTestLab, nous aidons les organisations à mettre "
"en place des processus de test structurés qui améliorent la communication, "
"réduisent les risques et livrent des produits logiciels fiables."'''),
    ],

    "nl": [
        ('msgid "QA planning meeting"\nmsgstr ""',
         'msgid "QA planning meeting"\nmsgstr "QA-planningsvergadering"'),

        ('msgid "Quality Through Collaboration"\nmsgstr ""',
         'msgid "Quality Through Collaboration"\nmsgstr "Kwaliteit door samenwerking"'),

        ('''msgid ""
"Successful software quality is built through strong collaboration between "
"testers, developers, business stakeholders, and project managers. At "
"SolutionsTestLab, we help organizations create structured testing processes "
"that improve communication, reduce risks, and deliver reliable software "
"products."
msgstr ""''',
         '''msgid ""
"Successful software quality is built through strong collaboration between "
"testers, developers, business stakeholders, and project managers. At "
"SolutionsTestLab, we help organizations create structured testing processes "
"that improve communication, reduce risks, and deliver reliable software "
"products."
msgstr ""
"Succesvolle softwarekwaliteit ontstaat door een sterke samenwerking tussen "
"testers, ontwikkelaars, zakelijke belanghebbenden en projectmanagers. Bij "
"SolutionsTestLab helpen wij organisaties gestructureerde testprocessen op "
"te zetten die de communicatie verbeteren, risico’s verminderen en "
"betrouwbare softwareproducten opleveren."'''),
    ],
}

for lang, pairs in replacements.items():
    path = Path(f"locale/{lang}/LC_MESSAGES/django.po")
    text = path.read_text(encoding="utf-8")

    for old, new in pairs:
        text = text.replace(old, new)

    path.write_text(text, encoding="utf-8")
    print(f"Fixed {lang}")

