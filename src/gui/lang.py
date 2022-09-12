# -*- coding:utf-8 -*-
#
# Copyright © 2016–2017 Liang Feng <finalion@gmail.com>
#
# Support: Report an issue at https://github.com/finalion/WordQuery/issues
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version; http://www.gnu.org/copyleft/gpl.html.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from anki.lang import currentLang

trans = {
    "CHECK_FILENAME_LABEL": {
        "zh_CN": "使用文件名作为标签",
        "en": "Use filename as dict label",
        "fr": r"Utiliser le nom de fichier en tant qu'étiquette de dico",
    },
    "EXPORT_MEDIA": {
        "zh_CN": "导出媒体文件",
        "en": "Export media files",
        "fr": "Exporter les fichiers multimédias",
    },
    "DICTS_FOLDERS": {"zh_CN": "字典文件夹", "en": "Dict folders", "fr": "Dossiers dico"},
    "CHOOSE_NOTE_TYPES": {
        "zh_CN": "选择笔记类型",
        "en": "Choose note types",
        "fr": "Choisir le type de note ",
    },
    "CURRENT_NOTE_TYPE": {
        "zh_CN": "当前类型",
        "en": "Current type",
        "fr": "Type utilisé en cours",
    },
    "MDX_SERVER": {"zh_CN": "MDX服务器", "en": "MDX server", "fr": "serveur MDX"},
    "USE_DICTIONARY": {"zh_CN": "使用字典", "en": "Use dict", "fr": "Utilisé un dico"},
    "UPDATED": {"zh_CN": "更新", "en": "Updated", "fr": "Mettre à jour"},
    "CARDS": {"zh_CN": "卡片", "en": "Cards", "fr": "Cartes"},
    "QUERIED": {"zh_CN": "查询", "en": "Queried", "fr": "Quêté"},
    "FIELDS": {"zh_CN": "字段", "en": "Fields", "fr": "Champs"},
    "WORDS": {"zh_CN": "单词", "en": "Words", "fr": "Mots"},
    "NOT_DICT_FIELD": {
        "zh_CN": "不是字典字段",
        "en": "Not dict field",
        "fr": "Pas un champ de dico",
    },
    "NOTE_TYPE_FIELDS": {
        "zh_CN": "<b>笔记字段</b>",
        "en": "<b>Note fields</b>",
        "fr": "<b>Champ de note</b>",
    },
    "DICTS": {"zh_CN": "<b>字典</b>", "en": "<b>Dict</b>", "fr": "<b>Dico</b>"},
    "DICT_FIELDS": {
        "zh_CN": "<b>字典字段</b>",
        "en": "<b>Dict fields</b>",
        "fr": "<b>Champ de dico</b>",
    },
    "RADIOS_DESC": {
        "zh_CN": "<b>单选框选中为待查询单词字段</b>",
        "en": "<b>Word field needs to be selected.</b>",
        "fr": "<b>Champ de mot doit d'être sélectionné. </b>",
    },
    "NO_QUERY_WORD": {
        "zh_CN": "查询字段无单词",
        "en": "No word is found in the query field",
        "fr": "Aucun est trouvé dans le champ",
    },
    "CSS_NOT_FOUND": {
        "zh_CN": "没有找到CSS文件，请手动选择",
        "en": "No valid css stylesheets found, please choose the file",
        "fr": "Aucun fichier de style CSS est valide, veuillez choisir le fichier",
    },
    "ABOUT": {"zh_CN": "关于", "en": "About", "fr": "À propos"},
    "REPOSITORY": {
        "zh_CN": "项目地址",
        "en": "Project homepage",
        "fr": "Accueil du projet",
    },
    "FEEDBACK": {"zh_CN": "反馈", "en": "Feedback", "fr": "Retourner de l'information"},
    "VERSION": {"zh_CN": "版本", "en": "Version", "fr": "Version"},
    "LATEST_VERSION": {
        "zh_CN": "无更新版本.",
        "en": "No update version.",
        "fr": "Pas de mise à jour.",
    },
    "ABNORMAL_VERSION": {
        "zh_CN": "当前版本异常.",
        "en": "The current version is abnormal.",
        "fr": "La version actuelle est anormale.",
    },
    "CHECK_FAILURE": {
        "zh_CN": "版本检查失败.",
        "en": "Version check failure.",
        "fr": "Erreur de vérifier la version.",
    },
    "NEW_VERSION": {
        "zh_CN": "检查到新版本:",
        "en": "New version:",
        "fr": "Nouvelle version:",
    },
    "UPDATE": {"zh_CN": "更新", "en": "Update", "fr": "Mise à jour"},
    "FORCE_UPDATE": {
        "zh_CN": "强制更新字段",
        "en": "Force update",
        "fr": "Mise à jour forcée",
    },
    "SETTINGS": {"zh_CN": "参数", "en": "Settings", "fr": "Paramètres"},
}

# This function will throw a deprication error, as gettext is not used in Anki anymore and Project Fluent is being used.
# However currently there's no other way for addons to be translated so while it works I'll let it be.
def _(key, lang=currentLang):
    if key not in trans:
        return key.lower().capitalize()

    if lang not in trans[key]:
        lang = "en"  # fallback

    return trans[key][lang]


def _sl(key):
    return trans[key].values()
