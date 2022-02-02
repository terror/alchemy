use std::cmp::PartialOrd;

#[derive(Debug)]
struct Point<T, U> {
  x: T,
  y: U,
}

impl<T, U> Point<T, U> {
  fn new(x: T, y: U) -> Point<T, U> {
    Self { x, y }
  }

  fn x(&self) -> &T {
    &self.x
  }

  fn y(&self) -> &U {
    &self.y
  }
}

fn largest<T: PartialOrd + Copy>(l: &[T]) -> T {
  let mut largest = l[0];

  for &item in l {
    if item > largest {
      largest = item;
    }
  }

  largest
}

fn main() {
  let a = Point::new("abc", 123);
  let b = Point::new(123, "abc");
  println!("{:?} {:?}", a, b);
}

#[cfg(test)]
mod tests {
  use super::*;

  #[test]
  fn largest_integer() {
    let integers = vec![1, 2, 3];
    assert_eq!(largest(&integers), 3);
  }

  #[test]
  fn largest_character() {
    let chars = vec!["a", "b", "c"];
    assert_eq!(largest(&chars), "c");
  }
}
