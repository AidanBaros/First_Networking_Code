import sys
import selectors
import json
import io
import struct

class Message:
    def __init__(self, selector, sock, addr) -> None:
        pass

    def process_events(self,mask):
        if mask & selectors.EVENT_READ:
            self.read()
        if mask & selectors.EVENT_WRITE:
            self.write()

    def read(self):
        self._read()
        if self._jsonheader_len is None:
            self.process_protoheader()
        
        if self._jsonheader_len is not None:
            if self.jsonheader is None:
                self.process_jsonheader()
        
        if self.jsonheader:
            if self.request is None:
                self.process_response()