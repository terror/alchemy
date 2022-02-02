use std::{sync::mpsc::channel, thread};

static NT: i32 = 5;

fn a() {
  // Two endpoints: Sender<T> & Receiver<T>
  // T -> type of the transfer message
  //
  // In this case we are dealing with Sender<i32> & Receiver<i32>
  // implicitly.
  let (tx, rx) = channel();
  let mut children = Vec::new();

  for id in 1..NT + 1 {
    // The Sender can be cloned to send to the same channel multiple times, but only one Receiver is supported.
    // https://doc.rust-lang.org/std/sync/mpsc/fn.channel.html
    let thread_tx = tx.clone();

    // Send over its id via the channel each thread
    let child = thread::spawn(move || {
      thread_tx.send(id).unwrap();
      println!("thread {} done!", id);
    });

    children.push(child);
  }

  let mut ids = Vec::with_capacity(NT as usize);
  for _ in 0..NT {
    // `recv` picks a message from the channel
    // it will block the current thread if no messages are available
    // https://doc.rust-lang.org/std/sync/mpsc/struct.Receiver.html
    ids.push(rx.recv());
  }

  // wait for each thread to finish
  for child in children {
    child.join().unwrap();
  }

  println!("{:?}", ids);

  // thread 2 done!
  // thread 4 done!
  // thread 5 done!
  // thread 3 done!
  // thread 1 done!
  // [Ok(4), Ok(2), Ok(3), Ok(1), Ok(5)]
}

fn b() {
  let (tx, rx) = channel();

  thread::spawn(move || {
    tx.send(1 + 1).unwrap();
  });

  println!("{:?}", rx.recv().unwrap()); // 2
}

fn main() {
  println!("--- A ---");
  a();

  println!();

  println!("--- B ---");
  b();
}
