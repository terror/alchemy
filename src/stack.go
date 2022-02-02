package main

import "fmt"

type Stack []string

func (s *Stack) IsEmpty() bool {
  return len(*s) == 0
}

func (s *Stack) Push(str string) {
  *s = append(*s, str)
}

func (s *Stack) Pop() (string, bool) {
  if s.IsEmpty() {
    return "", false
  } else {
    idx := len(*s) - 1
    el := (*s)[idx]
    *s = (*s)[:idx]
    return el, true
  }
}

func main() {
  var st Stack

  st.Push("Hello");
  st.Push("World");
  st.Push("!");

  if len(st) > 0 {
    for !st.IsEmpty() {
      x, y := st.Pop()
      if y == true {
        fmt.Println(x);
      }
    }
  }

  // !
  // World
  // Hello
}
