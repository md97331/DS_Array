class ArrayList:
    def __init__(self):
        self.data = ConstrainedList() # don't change this line!

    
    ### subscript-based access ###
    
    def _normalize_idx(self, idx):
        nidx = idx
        if nidx < 0:
            nidx += len(self.data)
            if nidx < 0:
                nidx = 0
        return nidx
    
    def __getitem__(self, idx):
        """Implements `x = self[idx]`"""
        assert(isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= len(self.data):
            raise IndexError
        return self.data[nidx]

    def __setitem__(self, idx, value):
        """Implements `self[idx] = x`"""
        assert(isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= len(self.data):
            raise IndexError
        self.data[nidx] = value

    def __delitem__(self, idx):
        """Implements `del self[idx]`"""
        assert(isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= len(self.data):
            raise IndexError
        for i in range(nidx+1, len(self.data)):
            self.data[i-1] = self.data[i]
        del self.data[len(self.data)-1]
    

    ### stringification ###
    
    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""
        strl = "["
        for x in range(len(self.data)):
            if (x==len(self.data)+1 or x==0):
                strl = ''.join((strl,str(self.data[x])))
            else:
                strl = ', '.join((strl,str(self.data[x])))
        strl += "]"
        
        return strl

    def __repr__(self):
        """Supports REPL inspection. (Same behavior as `str`.)"""
        strl = "["
        for x in range(len(self.data)):
            if (x==len(self.data)+1 or x==0):
                strl = ''.join((strl,str(self.data[x])))
            else:
                strl = ', '.join((strl,str(self.data[x])))
        strl += "]"  
        
        return strl

    ### single-element manipulation ###
    
    def append(self, value):
        """Appends value to the end of this list.""" #[1,2,3,4,5,6,7,8,9]
        self.data.append(None)
        idx = len(self.data)-1
        self.data[idx]=value
    
    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements down the
        list, as needed. Note that inserting a value at len(self) --- equivalent
        to appending the value --- is permitted. Raises IndexError if idx is invalid."""
        nidx = self._normalize_idx(idx)
        if nidx<0 or nidx>len(self.data):
            raise IndexError
        self.data.append(None)
        for n in range(len(self.data)-1,nidx,-1):
            self.data[n]=self.data[n-1]
        self.data[nidx] = value


    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""
        nidx = self._normalize_idx(idx)
        val = self.data[nidx]
        self.__delitem__(nidx)
        return val
    
    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""
        idx = -1
        findIt = False
        for i in range(len(self.data)):
            idx += 1
            if (self.data[i]==value):
                nidx = self._normalize_idx(idx)
                self.__delitem__(nidx)
                findIt = True
                break
        if (findIt==False):
            raise ValueError

    ### predicates (T/F queries) ###
    
    def __eq__(self, other):
        """Returns True if this ArrayList contains the same elements (in order) as other. If other is not an ArrayList, returns False."""
        if (len(self.data)!=len(other.data)):
            return False
        else:
            for i in range(len(self.data)):
                if(self.data[i] != other.data[i]):
                    return False
            return True
        

    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this list."""
        for i in range(len(self.data)):
            if(self.data[i] == value):
                return True
        return False


    ### queries ###
    
    def __len__(self):
        """Implements `len(self)`"""
        return len(self.data)
    
    def min(self):
        """Returns the minimum value in this list."""
        min=self.data[0]
        for i in range(len(self.data)):
            if(self.data[i]<min):
                min = self.data[i]
        return min

    def max(self):
        """Returns the maximum value in this list."""
        max=self.data[0]
        for i in range(len(self.data)):
            if(self.data[i]>max):
                max = self.data[i]
        return max
    
    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""
        limI = self._normalize_idx(i)
        if (j==None):
            limS = len(self.data)
        else:
            limS = self._normalize_idx(j)
        
        if(limI<0 or limI>len(self.data) or limS<0 or limS> len(self.data)):
            raise ValueError
        else:
            for i in range(limI, limS):
                if(self.data[i] == value):
                    return i
            raise ValueError
    
    def count(self, value):
        """Returns the number of times value appears in this list."""
        times = 0
        for i in range(len(self.data)):
            if(self.data[i] == value):
                    times += 1
        return times
    
    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_array_list`. Returns a new ArrayList
        instance that contains the values in this list followed by those 
        of other."""
        newArrayList = ArrayList()
        for j in range(len(self.data)):
            newArrayList.append(self.data[j])
        for i in range(len(other)):
            newArrayList.append(other[i])
        return newArrayList
        
    https://github.com/md97331/DS_Array/tree/main
    def clear(self):
        self.data = ConstrainedList() # don't change this!
        
    def copy(self):
        """Returns a new ArrayList instance (with a separate data store), that
        contains the same values as this list."""
        new = ArrayList()
        for i in range(len(self.data)):
            new.append(self.data[i])
        return new

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this list."""
        for i in range(len(other)):
            self.append(other[i])

            
    ### iteration ###
    
    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        class ArrayListIterator:
            def __init__(self, ConstrainedList):
                self.idx = 0
                self.lst = ConstrainedList
            def __iter__(self):
                return self
                
            def __next__(self):
                if self.idx<len(self.lst):
                    self.idx+=1
                    return self.lst.data[self.idx-1]
                else:
                    raise StopIteration()
        return ArrayListIterator(self)
