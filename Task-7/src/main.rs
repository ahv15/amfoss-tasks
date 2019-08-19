extern crate regex;
use regex::Regex;

fn main() {
  println!("Enter your email id ");

  let mut email = String::new();

  std::io::stdin().read_line(&mut email).unwrap();
    

  let re = Regex::new(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$").unwrap();
  println!("Is it a valid email? {}", re.is_match(email));
}


