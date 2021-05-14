import sys
import xml.dom
from typing import IO, Any, Optional, Text as _Text, TypeVar, Union
from xml.dom.xmlbuilder import DocumentLS, DOMImplementationLS
from xml.sax.xmlreader import XMLReader

_T = TypeVar("_T")

def parse(file: Union[str, IO[Any]], parser: Optional[XMLReader] = ..., bufsize: Optional[int] = ...): ...
def parseString(string: Union[bytes, _Text], parser: Optional[XMLReader] = ...): ...
def getDOMImplementation(features=...): ...

class Node(xml.dom.Node):
    namespaceURI: Optional[str]
    parentNode: Any
    ownerDocument: Any
    nextSibling: Any
    previousSibling: Any
    prefix: Any
    def toxml(self, encoding: Optional[Any] = ...): ...
    def toprettyxml(self, indent: str = ..., newl: str = ..., encoding: Optional[Any] = ...): ...
    def hasChildNodes(self) -> bool: ...
    def insertBefore(self, newChild, refChild): ...
    def appendChild(self, node): ...
    def replaceChild(self, newChild, oldChild): ...
    def removeChild(self, oldChild): ...
    def normalize(self) -> None: ...
    def cloneNode(self, deep): ...
    def isSupported(self, feature, version): ...
    def isSameNode(self, other): ...
    def getInterface(self, feature): ...
    def getUserData(self, key): ...
    def setUserData(self, key, data, handler): ...
    childNodes: Any
    def unlink(self) -> None: ...
    def __enter__(self: _T) -> _T: ...
    def __exit__(self, et, ev, tb) -> None: ...

class DocumentFragment(Node):
    nodeType: Any
    nodeName: str
    nodeValue: Any
    attributes: Any
    parentNode: Any
    childNodes: Any
    def __init__(self) -> None: ...

class Attr(Node):
    name: str
    nodeType: Any
    attributes: Any
    specified: bool
    ownerElement: Any
    namespaceURI: Optional[str]
    childNodes: Any
    nodeName: Any
    nodeValue: str
    value: str
    prefix: Any
    def __init__(
        self, qName: str, namespaceURI: Optional[str] = ..., localName: Optional[Any] = ..., prefix: Optional[Any] = ...
    ) -> None: ...
    def unlink(self) -> None: ...

class NamedNodeMap:
    def __init__(self, attrs, attrsNS, ownerElement) -> None: ...
    def item(self, index): ...
    def items(self): ...
    def itemsNS(self): ...
    def __contains__(self, key): ...
    def keys(self): ...
    def keysNS(self): ...
    def values(self): ...
    def get(self, name, value: Optional[Any] = ...): ...
    def __len__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __getitem__(self, attname_or_tuple): ...
    def __setitem__(self, attname, value) -> None: ...
    def getNamedItem(self, name): ...
    def getNamedItemNS(self, namespaceURI: str, localName): ...
    def removeNamedItem(self, name): ...
    def removeNamedItemNS(self, namespaceURI: str, localName): ...
    def setNamedItem(self, node): ...
    def setNamedItemNS(self, node): ...
    def __delitem__(self, attname_or_tuple) -> None: ...

AttributeList = NamedNodeMap

class TypeInfo:
    namespace: Any
    name: Any
    def __init__(self, namespace, name) -> None: ...

class Element(Node):
    nodeType: Any
    nodeValue: Any
    schemaType: Any
    parentNode: Any
    tagName: str
    prefix: Any
    namespaceURI: Optional[str]
    childNodes: Any
    nextSibling: Any
    def __init__(
        self, tagName, namespaceURI: Optional[str] = ..., prefix: Optional[Any] = ..., localName: Optional[Any] = ...
    ) -> None: ...
    def unlink(self) -> None: ...
    def getAttribute(self, attname): ...
    def getAttributeNS(self, namespaceURI: str, localName): ...
    def setAttribute(self, attname, value) -> None: ...
    def setAttributeNS(self, namespaceURI: str, qualifiedName: str, value) -> None: ...
    def getAttributeNode(self, attrname): ...
    def getAttributeNodeNS(self, namespaceURI: str, localName): ...
    def setAttributeNode(self, attr): ...
    setAttributeNodeNS: Any
    def removeAttribute(self, name) -> None: ...
    def removeAttributeNS(self, namespaceURI: str, localName) -> None: ...
    def removeAttributeNode(self, node): ...
    removeAttributeNodeNS: Any
    def hasAttribute(self, name: str) -> bool: ...
    def hasAttributeNS(self, namespaceURI: str, localName) -> bool: ...
    def getElementsByTagName(self, name): ...
    def getElementsByTagNameNS(self, namespaceURI: str, localName): ...
    def writexml(self, writer, indent: str = ..., addindent: str = ..., newl: str = ...) -> None: ...
    def hasAttributes(self) -> bool: ...
    def setIdAttribute(self, name) -> None: ...
    def setIdAttributeNS(self, namespaceURI: str, localName) -> None: ...
    def setIdAttributeNode(self, idAttr) -> None: ...

class Childless:
    attributes: Any
    childNodes: Any
    firstChild: Any
    lastChild: Any
    def appendChild(self, node) -> None: ...
    def hasChildNodes(self) -> bool: ...
    def insertBefore(self, newChild, refChild) -> None: ...
    def removeChild(self, oldChild) -> None: ...
    def normalize(self) -> None: ...
    def replaceChild(self, newChild, oldChild) -> None: ...

class ProcessingInstruction(Childless, Node):
    nodeType: Any
    target: Any
    data: Any
    def __init__(self, target, data) -> None: ...
    nodeValue: Any
    nodeName: Any
    def writexml(self, writer, indent: str = ..., addindent: str = ..., newl: str = ...) -> None: ...

class CharacterData(Childless, Node):
    ownerDocument: Any
    previousSibling: Any
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    data: str
    nodeValue: Any
    def substringData(self, offset: int, count: int) -> str: ...
    def appendData(self, arg: str) -> None: ...
    def insertData(self, offset: int, arg: str) -> None: ...
    def deleteData(self, offset: int, count: int) -> None: ...
    def replaceData(self, offset: int, count: int, arg: str) -> None: ...

class Text(CharacterData):
    nodeType: Any
    nodeName: str
    attributes: Any
    data: Any
    def splitText(self, offset): ...
    def writexml(self, writer, indent: str = ..., addindent: str = ..., newl: str = ...) -> None: ...
    def replaceWholeText(self, content): ...

class Comment(CharacterData):
    nodeType: Any
    nodeName: str
    def __init__(self, data) -> None: ...
    def writexml(self, writer, indent: str = ..., addindent: str = ..., newl: str = ...) -> None: ...

class CDATASection(Text):
    nodeType: Any
    nodeName: str
    def writexml(self, writer, indent: str = ..., addindent: str = ..., newl: str = ...) -> None: ...

class ReadOnlySequentialNamedNodeMap:
    def __init__(self, seq=...) -> None: ...
    def __len__(self): ...
    def getNamedItem(self, name): ...
    def getNamedItemNS(self, namespaceURI: str, localName): ...
    def __getitem__(self, name_or_tuple): ...
    def item(self, index): ...
    def removeNamedItem(self, name) -> None: ...
    def removeNamedItemNS(self, namespaceURI: str, localName) -> None: ...
    def setNamedItem(self, node) -> None: ...
    def setNamedItemNS(self, node) -> None: ...

class Identified: ...

class DocumentType(Identified, Childless, Node):
    nodeType: Any
    nodeValue: Any
    name: Any
    publicId: Any
    systemId: Any
    internalSubset: Any
    entities: Any
    notations: Any
    nodeName: Any
    def __init__(self, qualifiedName: str) -> None: ...
    def cloneNode(self, deep): ...
    def writexml(self, writer, indent: str = ..., addindent: str = ..., newl: str = ...) -> None: ...

class Entity(Identified, Node):
    attributes: Any
    nodeType: Any
    nodeValue: Any
    actualEncoding: Any
    encoding: Any
    version: Any
    nodeName: Any
    notationName: Any
    childNodes: Any
    def __init__(self, name, publicId, systemId, notation) -> None: ...
    def appendChild(self, newChild) -> None: ...
    def insertBefore(self, newChild, refChild) -> None: ...
    def removeChild(self, oldChild) -> None: ...
    def replaceChild(self, newChild, oldChild) -> None: ...

class Notation(Identified, Childless, Node):
    nodeType: Any
    nodeValue: Any
    nodeName: Any
    def __init__(self, name, publicId, systemId) -> None: ...

class DOMImplementation(DOMImplementationLS):
    def hasFeature(self, feature, version) -> bool: ...
    def createDocument(self, namespaceURI: str, qualifiedName: str, doctype): ...
    def createDocumentType(self, qualifiedName: str, publicId, systemId): ...
    def getInterface(self, feature): ...

class ElementInfo:
    tagName: Any
    def __init__(self, name) -> None: ...
    def getAttributeType(self, aname): ...
    def getAttributeTypeNS(self, namespaceURI: str, localName): ...
    def isElementContent(self): ...
    def isEmpty(self): ...
    def isId(self, aname): ...
    def isIdNS(self, namespaceURI: str, localName): ...

class Document(Node, DocumentLS):
    implementation: Any
    nodeType: Any
    nodeName: str
    nodeValue: Any
    attributes: Any
    parentNode: Any
    previousSibling: Any
    nextSibling: Any
    actualEncoding: Any
    encoding: Any
    standalone: Any
    version: Any
    strictErrorChecking: bool
    errorHandler: Any
    documentURI: Any
    doctype: Any
    childNodes: Any
    def __init__(self) -> None: ...
    def appendChild(self, node): ...
    documentElement: Any
    def removeChild(self, oldChild): ...
    def unlink(self) -> None: ...
    def cloneNode(self, deep): ...
    def createDocumentFragment(self): ...
    def createElement(self, tagName: str): ...
    def createTextNode(self, data): ...
    def createCDATASection(self, data): ...
    def createComment(self, data): ...
    def createProcessingInstruction(self, target, data): ...
    def createAttribute(self, qName) -> Attr: ...
    def createElementNS(self, namespaceURI: str, qualifiedName: str): ...
    def createAttributeNS(self, namespaceURI: str, qualifiedName: str) -> Attr: ...
    def getElementById(self, id): ...
    def getElementsByTagName(self, name: str): ...
    def getElementsByTagNameNS(self, namespaceURI: str, localName): ...
    def isSupported(self, feature, version): ...
    def importNode(self, node, deep): ...
    def writexml(
        self, writer, indent: str = ..., addindent: str = ..., newl: str = ..., encoding: Optional[Any] = ...
    ) -> None: ...
    def renameNode(self, n, namespaceURI: str, name): ...
