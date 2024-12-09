object Day03 extends App {
  val input = scala.io.Source
    .fromFile("../inputs/2024/day_03.txt")
    .mkString
    .replace("\n", "")

  val partOneSolution: Int = solvePartOne(input)
  val partTwoSolution: Int = solvePartTwo(input)

  println(f"Part 1: $partOneSolution")
  println(f"Part 2: $partTwoSolution")

  def solvePartOne(input: String): Int = {
    """mul\((\d+),(\d+)\)""".r
      .findAllMatchIn(input)
      .map { m =>
        m.group(1).toInt * m.group(2).toInt
      }
      .sum
  }

  def solvePartTwo(input: String): Int = {
    """mul\((\d+),(\d+)\)""".r
      .findAllMatchIn("""don't\(\).*?(?:do\(\)|$)""".r.replaceAllIn(input, ""))
      .map { m =>
        m.group(1).toInt * m.group(2).toInt
      }
      .sum
  }
}
