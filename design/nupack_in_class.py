import string
from generic_classes import ordered_dict, PrintObject
from DNA_classes import *

class Spec(PrintObject):
  def __init__(self):
    self.complexes = self.structs = ordered_dict()
    self.seqs = ordered_dict()
  
  def add_structure(self, (name, struct)):
    assert not self.structs.has_key(name), "Duplicate structure definition"
    self.structs[name] = Structure(name, struct)
  def add_sequence(self, (name, const)):
    assert not self.seqs.has_key(name), "Duplicate sequence definition"
    num = len(self.seqs)
    self.seqs[name] = Sequence(name, const, num)
  def add_apply(self, (struct, seqs)):
    struct.set_seqs(seqs)
