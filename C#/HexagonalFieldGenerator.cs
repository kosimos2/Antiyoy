using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;

public class HexagonalFieldGenerator : MonoBehaviour
{
    public GameObject hexagonPrefab;
    public float gridWidth;
    public float gridHeight;

    void Start()
    {
        GenerateHexagonalField();
    }

    void GenerateHexagonalField()
    {
        for (int x = 0; x < gridWidth; x++)
        {
            
            for (int y = 0; y < gridHeight; y++)
            {
                
                Vector3 spawnPosition = CalculateHexagonPosition(x, y);
                GameObject hexcraet = Instantiate(hexagonPrefab, spawnPosition, Quaternion.identity, transform);
                // Дополнительная настройка свойств гексагона, если необходимо
             
            }
        }
    }

    Vector3 CalculateHexagonPosition(float a, float b)
    {
        float rad = 1;
        float x = a * (rad * 2);
        float y = 0;
        for (int i = 0; i < b; i++)
        {
            x += 1 * rad;
            y += 2 * rad;
        }
        return new Vector3(x, y);
    }
}

