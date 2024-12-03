object Day01 extends App {
  val input = scala.io.Source.fromFile("../../inputs/2024/day_01.txt").mkString

  val (left, right) = parse_input(input)

  val part_1_solution = solve_part_1(left, right)
  val part_2_solution = solve_part_2(left, right)

  println(f"Part 1: $part_1_solution")
  println(f"Part 2: $part_2_solution")

  def solve_part_1(left: Seq[Int], right: Seq[Int]): Int = {
    left.zip(right).map((left, right) => ((left - right).abs)).sum
  }

  def solve_part_2(left: Seq[Int], right: Seq[Int]): Int = {
    left.map((item) => item * right.count(_ == item)).sum
  }

  def parse_input(input: String): (Seq[Int], Seq[Int]) = {
    val input_split =
      input.linesIterator.map(_.split("   ").map(_.toInt)).toSeq

    val left = input_split.map(_(0)).sorted
    val right = input_split.map(_(1)).sorted

    (left, right)
  }

}
