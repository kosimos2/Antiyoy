using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Hexcraet : MonoBehaviour
{
    public LineRenderer lineRenderer;
    public float width = 0.1f;
    public Color startColor = Color.red;
    public Color endColor = Color.blue;

    private Vector3[] points = new Vector3[6];


    // Start is called before the first frame update
    void Start()
    {
        lineRenderer = GetComponent<LineRenderer>();
        lineRenderer.positionCount = 6;
        lineRenderer.startColor = startColor;
        lineRenderer.endColor = endColor;
        //lineRenderer.loop = true;
        
        CalculateHexagonSides(0, 0, 5);
        CalculateHexagonSides(20, 20, 5);
    }

    public List<Tuple<float, float, float, float>> CalculateHexagonSides(float centerX, float centerY, float sideLength)
    {
        List<Tuple<float, float, float, float>> sides = new List<Tuple<float, float, float, float>>();
        double angle = 60;
        for (int i = 0; i < 6; i++)
        {
            double start_x = centerX + sideLength * Math.Cos(Math.PI / 180 * angle * i);
            double start_y = centerY + sideLength * Math.Sin(Math.PI / 180 * angle * i);
            double end_x = centerX + sideLength * Math.Cos(Math.PI / 180 * angle * (i + 1));
            double end_y = centerY + sideLength * Math.Sin(Math.PI / 180 * angle * (i + 1));
            sides.Add(new Tuple<float, float, float, float>((float)start_x, (float)start_y, (float)end_x, (float)end_y));            
            points[i] = new Vector3(sides[i].Item1, sides[i].Item2, 0);
            lineRenderer.SetPositions(points);

        }      
        return sides;
    }

    public static void Main(Vector3[] points, LineRenderer lineRenderer)
    {
           
    }
    



    // Update is called once per frame
    void Update()
    {
        



    }
}
