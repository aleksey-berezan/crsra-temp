using System;
using System.Collections;
using System.Linq;
using System.Runtime.CompilerServices;

namespace ConsoleApp1
{
    internal sealed class LongPoint
    {
        public static readonly Func<LongPoint, long> ByX = p => p.X;
        public static readonly Func<LongPoint, long> ByY = p => p.Y;

        public readonly long X;
        public readonly long Y;

        public LongPoint(long x, long y)
        {
            X = x;
            Y = y;
        }

        public override string ToString()
        {
            return string.Format("{0}:{1}", X, Y);
        }
    }

    internal sealed class PointComparer : IComparer
    {
        public int Compare(object x, object y)
        {
            LongPoint p1 = (LongPoint)x;
            LongPoint p2 = (LongPoint)y;
            return (int)((p1.X != p2.X ? p1.X - p2.X : p1.Y - p2.Y) % int.MaxValue);
        }
    }

    static class Closest
    {
        static void Main(string[] args)
        {
            LongPoint[] points = ParsePoints();
            Array.Sort(points, new PointComparer());
            double distance = MinDistance(points);
            Console.WriteLine("{0:0.000000000}", distance);
        }

        private static LongPoint[] ParsePoints()
        {
            string line = Console.ReadLine();
            int n = int.Parse(line);
            LongPoint[] points = new LongPoint[n];
            int i = 0;
            while (!string.IsNullOrEmpty((line = Console.ReadLine())))
            {
                string[] ss = line.Split(' ');
                var point = new LongPoint(long.Parse(ss[0]), long.Parse(ss[1]));
                points[i] = point;
                i++;
            }

            if (i != n)
            {
                throw new Exception(n + " points expected but only " + i + " parsed.");
            }

            return points;
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        private static double Distance(LongPoint p1, LongPoint p2)
        {
            return Math.Sqrt((p1.X - p2.X) * (p1.X - p2.X) + (p1.Y - p2.Y) * (p1.Y - p2.Y));
        }

        private static double MinDistance(LongPoint[] points)
        {
            if (points.Length <= 1)
            {
                return double.MaxValue;
            }

            if (points.Length == 2)
            {
                return Distance(points[0], points[1]);
            }

            double minDistance;
            if (points.Length <= 10)
            {
                minDistance = Distance(points[0], points[1]);
                for (int i = 0; i < points.Length; i++)
                {
                    LongPoint p1 = points[i];
                    for (int j = i + 1; j < points.Length; j++)
                    {
                        LongPoint p2 = points[j];
                        {
                            minDistance = Math.Min(minDistance, Distance(p1, p2));
                        }
                    }
                }

                return minDistance;
            }

            Func<LongPoint, long> getCoordinate = LongPoint.ByY;
            double midPoint;
            LongPoint[] left, right;
            Split(points, getCoordinate, out midPoint, out left, out right);

            bool noSplit = left.Length == points.Length || right.Length == points.Length;
            if (noSplit)
            {
                // points share same y
                // go y
                getCoordinate = LongPoint.ByX;
                Split(points, getCoordinate, out midPoint, out left, out right);

                bool stillNoSplit = left.Length == points.Length || right.Length == points.Length;
                if (stillNoSplit)
                {
                    // great, same x's
                    return 0;
                }
            }

            double minLeft = MinDistance(left);
            double minRight = MinDistance(right);
            minDistance = Math.Min(minLeft, minRight);

            for (int i = 0; i < left.Length; i++)
            {
                LongPoint pLeft = left[i];
                if (Math.Abs(midPoint - getCoordinate(pLeft)) <= minDistance)
                {
                    for (int j = 0; j < right.Length; j++)
                    {
                        LongPoint pRight = right[j];
                        if (Math.Abs(midPoint - getCoordinate(pRight)) <= minDistance)
                        {
                            double d = Distance(pLeft, pRight);
                            minDistance = Math.Min(minDistance, d);
                        }
                    }
                }
            }

            return minDistance;
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        private static void Split(LongPoint[] points, Func<LongPoint, long> getCoordinate, out double midPoint, out LongPoint[] left, out LongPoint[] right)
        {
            double mid = (points.Max(getCoordinate) + points.Min(getCoordinate)) / 2.0d;
            left = points.Where(p => getCoordinate(p) <= mid).ToArray();
            right = points.Where(p => getCoordinate(p) > mid).ToArray();
            midPoint = mid;
        }
    }
}
