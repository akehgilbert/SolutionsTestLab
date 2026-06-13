from pathlib import Path

path = Path("locale/de/LC_MESSAGES/django.po")
text = path.read_text(encoding="utf-8")

replacements = {
'''msgid ""
"From quality strategy to test execution and governance, SolutionsTestLab "
"provides end-to-end software quality services that help organizations "
"release with confidence."
msgstr ""''':
'''msgid ""
"From quality strategy to test execution and governance, SolutionsTestLab "
"provides end-to-end software quality services that help organizations "
"release with confidence."
msgstr ""
"Von der Qualitätsstrategie bis zur Testausführung und Qualitätssteuerung "
"bietet SolutionsTestLab ganzheitliche Software-Qualitätsdienstleistungen, "
"die Unternehmen dabei helfen, Software mit Vertrauen zu veröffentlichen."''',

'''msgid ""
"Build quality into every stage of software delivery through QA strategy, "
"process improvement, defect prevention, and release readiness."
msgstr ""''':
'''msgid ""
"Build quality into every stage of software delivery through QA strategy, "
"process improvement, defect prevention, and release readiness."
msgstr ""
"Integrieren Sie Qualität in jede Phase der Softwareentwicklung durch "
"QA-Strategie, Prozessverbesserung, Fehlervermeidung und Release-Bereitschaft."''',

'''msgid ""
"Comprehensive manual and test automation services including functional, "
"regression, exploratory, API, and user acceptance testing."
msgstr ""
"Manuelle, funktionale, Regressions-, explorative und Benutzerakzeptanztests "
"für stabile Veröffentlichungen."''':
'''msgid ""
"Comprehensive manual and test automation services including functional, "
"regression, exploratory, API, and user acceptance testing."
msgstr ""
"Umfassende manuelle Test- und Testautomatisierungsleistungen einschließlich "
"funktionaler Tests, Regressionstests, explorativer Tests, API-Tests und "
"Benutzerakzeptanztests."''',

'''msgid ""
"Structured test planning, coordination, reporting, and quality governance to "
"ensure successful software releases."
msgstr ""
"Testmanagement ist die Planung, Koordination, Überwachung und Steuerung von "
"Testaktivitäten, um Softwarequalität und erfolgreiche Releases "''':
'''msgid ""
"Structured test planning, coordination, reporting, and quality governance to "
"ensure successful software releases."
msgstr ""
"Strukturierte Testplanung, Koordination, Berichterstattung und "
"Qualitätssteuerung zur Sicherstellung erfolgreicher Software-Releases."''',
}

for old, new in replacements.items():
    text = text.replace(old, new)

path.write_text(text, encoding="utf-8")
print("German Home Core section fixed.")
