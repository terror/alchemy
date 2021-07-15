#[cfg(test)]
use rstest::*;

#[cfg(test)]
struct Item {
  pub name:  String,
  pub price: i8,
}

#[cfg(test)]
impl Item {
  fn new(name: String, price: i8) -> Self {
    Self { name, price }
  }
}

#[cfg(test)]
fn fib(n: u32) -> u32 {
  match n {
    0 | 1 => n,
    _ => fib(n - 1) + fib(n - 2),
  }
}

fn main() {}

#[cfg(test)]
mod tests {
  use super::*;

  #[fixture]
  pub fn fixture() -> u32 {
    50
  }

  // mind blown
  #[fixture]
  fn item(#[default("A")] name: &str, #[default(10)] price: i8) -> Item {
    Item::new(name.into(), price)
  }

  #[rstest]
  fn ok(fixture: u32) {
    assert_eq!(fixture, 50)
  }

  #[rstest]
  #[case(0, 0)]
  #[case(1, 1)]
  #[case(2, 1)]
  #[case(3, 2)]
  #[case(4, 3)]
  fn fib_test(#[case] input: u32, #[case] expected: u32) {
    assert_eq!(fib(input), expected);
  }

  #[rstest]
  fn default(item: Item) {
    assert_eq!(item.name, "A");
    assert_eq!(item.price, 10);
  }

  #[rstest]
  fn with(#[with("B", 80)] item: Item) {
    assert_eq!(item.name, "B");
    assert_eq!(item.price, 80);
  }
}
