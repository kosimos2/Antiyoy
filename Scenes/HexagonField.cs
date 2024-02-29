using System;
using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class HexagonField : MonoBehaviour
{
    public GameObject hexagonPrefab;
    public int width;
    public int height;

    // Start is called before the first frame update
    void Start()
    {
        if (hexagonPrefab != null)
        {
            int number = 1;
            float hexagonWidth = hexagonPrefab.GetComponent<Renderer>().bounds.size.x;
            float hexagonHeight = hexagonPrefab.GetComponent<Renderer>().bounds.size.y;

            for (int x = 0; x < width; x++)
            {
                for (int y = 0; y < height; y++)
                {
                    GameObject hexagon = Instantiate(hexagonPrefab, transform);
                    hexagon.transform.position = new Vector3(x * hexagonWidth * 0.75f, y * hexagonHeight + ((x % 2 == 0) ? 0 : hexagonHeight * 0.5f), 0);
                    //hexagon.GetComponent<Hexagon>().number = number;
                    hexagon.name = "Hexagon " + number;
                    number++;
                }
            }
        }
        else
        {
            Debug.LogError("HexagonPrefab is not assigned!");
        }
    }



    // Update is called once per frame
    void Update()
    {

    }
}

