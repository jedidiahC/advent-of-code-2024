use std::{fs::File, io::{BufRead, BufReader}};

const INPUT_FILE: &str = "1/1.in";

fn main() {

    fn solve_part_one(reader: BufRead) -> Result<usize> {
        let lines = reader.lines();
        println!(lines);

    }

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = solve_part_one(input_file)
}
