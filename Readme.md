# xml2website

Generate a website and its associated directory and web pages on demand as described in a XML file.

## Usage

```
python xml2website.py
```

## Different XML Parsing Technology

XML APIs are either:

   - **DOM based** - the entire document is read into memory as a tree structure for random access by the calling application

OR

   - **Event based** - the application registers to receive events as entities are encountered within the source document.
  
   
### DOM (Document Object Model)

If you prefer this technique you should know that the whole XML will be loaded into memory. Advantage of this technique is you can navigate/read to any node. You can append, delete or update a child node because data is available in the memory. However if the XML contains a large data, then it will be very expensive to load it into memory. Also the whole XML is loaded to memory although you are looking for something particular.

You should consider using this technique, when you need to alter xml structure and you are sure that memory consumption is not going to be expensive. Also this is the only choice where you can navigate to parent and child elements. This makes it easier to use.

If you are creating a XML document (which is not big!) you should use this technique. However, if you are going to export a data from a database to xml (where you do not need navigation in the xml and/or data is huge) then you should consider other approaches.

DOM API is standardized by w3c. 

### SAX (Simple API for XML)

SAX has totally a different approach. It starts to read the XML document from beginning to end, but it does not store anything to memory. Instead it fires events and you can add your event handler depending on your requirements.

Your event handler will be called for example when an element begins or ends, when processing of document begins or ends. For all events please follow this link. 
So you register a handler (or more then one handler) and those handlers are called when an event occurs. 

### StAX (Streaming API for XML)

Both methods aforementioned have advantages: DOM, for example, allows for random access to the document, and SAX has a small memory footprint and is typically much faster. These two access metaphors can be thought of as polar opposites. A tree based API allows unlimited, random access and manipulation, while an event based API is a 'one shot' pass through the source document.

StAX is a newer technology then the others, StAX was designed as a median between these two opposites. In the StAX metaphor, the programmatic entry point is a cursor that represents a point within the document. The application moves the cursor forward - 'pulling' the information from the parser as it needs. This is different from an event based API - such as SAX - which 'pushes' data to the application - requiring the application to maintain state between events as necessary to keep track of location within the document.