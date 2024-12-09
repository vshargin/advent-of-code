object Day01 extends App {
  val input = scala.io.Source.fromFile("../inputs/2024/day_01.txt").mkString

  val (left, right) = parse_input(input)

  val partOneSolution = solvePartOne(left, right)
  val partTwoSolution = solvePartTwo(left, right)

  println(f"Part 1: $partOneSolution")
  println(f"Part 2: $partTwoSolution")

  def solvePartOne(left: Seq[Int], right: Seq[Int]): Int = {
    left.zip(right).map((left, right) => ((left - right).abs)).sum
  }

  def solvePartTwo(left: Seq[Int], right: Seq[Int]): Int = {
    left.map((item) => item * right.count(_ == item)).sum
  }

  def parse_input(input: String): (Seq[Int], Seq[Int]) = {
    val splitInput =
      input.linesIterator.map(_.split("   ").map(_.toInt)).toSeq

    val left = splitInput.map(_(0)).sorted
    val right = splitInput.map(_(1)).sorted

    (left, right)
  }

}
