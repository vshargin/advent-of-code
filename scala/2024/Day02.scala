object Day02 extends App {
  val input = scala.io.Source.fromFile("../inputs/2024/day_02.txt").mkString

  val reports = parseInput(input)

  val partOneSolution: Int = solvePartOne(reports)
  val partTwoSolution: Int = solvePartTwo(reports)

  println(f"Part 1: $partOneSolution")
  println(f"Part 2: $partTwoSolution")

  def solvePartOne(reports: Seq[Report]): Int = {
    reports.count(_.isSafe)
  }

  def solvePartTwo(reports: Seq[Report]): Int = {
    reports.count(_.isSafeWithDampener)
  }

  def parseInput(input: String): Seq[Report] = {
    input.linesIterator
      .map(_.split(" ").map(_.toInt).toSeq)
      .toSeq
      .map(Report(_))
  }

}

case class Report(sequence: Seq[Int]) {
  def isDecrease: Seq[Boolean] =
    sequence.zip(sequence.drop(1)).map((left, right) => (left > right))

  def isIncrease: Seq[Boolean] =
    sequence.zip(sequence.drop(1)).map((left, right) => (left < right))

  def isMonotonous: Boolean =
    isDecrease.forall(_ == true) || isIncrease.forall(_ == true)

  def isWithinDiffLimits: Boolean =
    sequence
      .zip(sequence.drop(1))
      .map((left, right) => (math.abs(left - right)))
      .forall((el) => (el > 0) && (el <= 3))

  def isSafe: Boolean =
    isMonotonous && isWithinDiffLimits
  
  def isSafeWithDampener: Boolean = 
    Range(0, sequence.length).map((i) => {
      val (left, right) = sequence.splitAt(i)
      val (middle, rightTail) = right.splitAt(1)
      val newSeq = left ++ rightTail
      Report(newSeq).isSafe
    }).contains(true)
}
