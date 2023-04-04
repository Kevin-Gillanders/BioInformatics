use std::{collections::HashMap, fs, iter::zip};

struct Matrix {
    data: Vec<Vec<String>>,
}

impl Matrix {
    fn new(data: Vec<String>) -> Self {
        // println!("New");

        let mut rows: Vec<Vec<String>> = vec![];

        for row in data {
            let mut row_data: Vec<String> = vec![];
            for cell in row.chars() {
                row_data.push(cell.to_string().to_ascii_uppercase());
                // println!("{}", cell);
            }
            rows.push(row_data);
            // println!();
        }

        Self { data: rows.clone() }
    }

    fn transpose(&self) -> Vec<Vec<String>>
// <T>(v: Vec<Vec<T>>) -> Vec<Vec<T>>
    // where
    //     T: Clone,
    {
        // println!("transpose");
        assert!(!self.data.is_empty());
        (0..self.data[0].len())
            .map(|i| {
                self.data
                    .iter()
                    .map(|inner| inner[i].clone())
                    .collect::<Vec<String>>()
            })
            .collect()
    }

    #[allow(dead_code)]
    fn print_matrix(data: &Vec<Vec<String>>) {
        for row in data {
            println!("{:?}", row);
        }
    }

    #[allow(dead_code)]
    fn print(&self, transpose: bool) {
        if transpose {
            Self::print_matrix(&self.transpose());
        } else {
            Self::print_matrix(&self.data);
        }
    }

    fn make_profile_matrix(&self) -> Vec<HashMap<String, i32>> {
        // println!("make_profile_matrix");

        let mut profile_matrix: Vec<HashMap<String, i32>> = vec![];

        for row in self.transpose() {
            let mut map: HashMap<String, i32> = Matrix::make_default_hashmap();
            for cell in &row {
                *map.entry(cell.to_owned()).or_default() += 1;
            }
            profile_matrix.push(map);
        }
        Matrix::print_profile_matrix(profile_matrix.clone());

        return profile_matrix;
    }

    fn make_consensus_string(&self) {
        // println!("make_consensus_string");

        let profile_matrix = Matrix::make_profile_matrix(&self);
        let mut consensus_string: Vec<String> = vec![];

        for char_count in profile_matrix {
            let x = char_count
                .iter()
                .max_by(|a, b| a.1.cmp(&b.1))
                .expect("No max value");

            consensus_string.push(x.0.clone());
        }

        for x in consensus_string {
            print!("{}", x);
        }
    }

    fn make_default_hashmap() -> HashMap<String, i32> {
        // println!("make_default_hashmap");

        let mut map: HashMap<String, i32> = HashMap::new();
        let _ = *map.entry("A".to_string()).or_insert(0);
        let _ = *map.entry("C".to_string()).or_insert(0);
        let _ = *map.entry("G".to_string()).or_insert(0);
        let _ = *map.entry("T".to_string()).or_insert(0);

        return map;
    }

    fn print_profile_matrix(profile_matrix: Vec<HashMap<String, i32>>) {
        // println!("print_profile_matrix");
        let mut a: (String, Vec<i32>) = ("A".to_string(), vec![]);
        let mut t: (String, Vec<i32>) = ("T".to_string(), vec![]);
        let mut c: (String, Vec<i32>) = ("C".to_string(), vec![]);
        let mut g: (String, Vec<i32>) = ("G".to_string(), vec![]);

        for row in profile_matrix {
            for cell in row {
                match cell.0.as_str() {
                    "A" => a.1.push(cell.1),
                    "T" => t.1.push(cell.1),
                    "C" => c.1.push(cell.1),
                    "G" => g.1.push(cell.1),
                    _ => println!("None"),
                }
            }
        }

        println!(
            "{}\n{}\n{}\n{}\n",
            format!("{}: {:?}", a.0, a.1)
                .replace("[", "")
                .replace(",", "")
                .replace("]", ""),
            format!("{}: {:?}", c.0, c.1)
                .replace("[", "")
                .replace(",", "")
                .replace("]", ""),
            format!("{}: {:?}", g.0, g.1)
                .replace("[", "")
                .replace(",", "")
                .replace("]", ""),
            format!("{}: {:?}", t.0, t.1)
                .replace("[", "")
                .replace(",", "")
                .replace("]", "")
        );
    }
}

fn read_fasta_file(file_name: &str) -> Vec<String> {
    let data =
        fs::read_to_string(file_name.to_string()).expect("There was an issue reading in the file");
    let mut fasta_data: Vec<String> = vec![];
    let mut line_data: String = String::new();

    let mut data_peek = data.split('\n').peekable();

    while let Some(line) = data_peek.next() {
        if line.starts_with('>') || data_peek.peek().is_none() {
            if line_data.is_empty() {
                continue;
            }
            if data_peek.peek().is_none() {
                line_data.push_str(line.trim());
            }
            fasta_data.push(line_data.trim().to_string());
            // println!("fasta data {:#?}", fasta_data);
            line_data = String::new();
            continue;
        } else {
            line_data.push_str(line.trim());
            // println!("Line data {}\n", line_data);
            // println!("Line {}\n", line);
        }
    }

    return fasta_data;
}

fn get_hamming_distance(string_1: &str, string_2: &str) -> i32 {
    let zipped_str = zip(string_1.chars(), string_2.chars());
    let mut count = 0;
    for c in zipped_str {
        println!("{:?}", c);
        if c.0 != c.1 {
            count += 1;
        }
    }

    return count;
}

fn main() {
    // env::set_var("RUST_BACKTRACE", "1");
    println!("Rosalind problem 8!");
    let data:Vec<&str> = fs::read_to_string("8_ex1.txt").expect("There was an issue reading in the file").split('\n').collect();
    
    let binding = fs::read_to_string("8_ex1.txt").expect("There was an issue reading in the file");
    let data:Vec<&str> = binding.split('\n').collect();

    println!("Hamming distance : {}", get_hamming_distance(data[0], data[1]));

    println!("Rosalind problem 9!");
    let x = Matrix::new(read_fasta_file("ex2.txt"));
    // x.print(false);
    // x.print(true);

    x.make_consensus_string();
}
