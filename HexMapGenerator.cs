using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Tilemaps;

public class HexMapGenerator : MonoBehaviour
{
    
    public Tilemap tilemap;
    public GameObject hexPrefab; 
    public int mapWidth;
    public int mapHeight;

    private float hexWidth = 2.598076f; // ������ ���������
    private float hexHeight = 2.25f; // ������ ���������


    // Start is called before the first frame update
    void Start()
    {
        GenerateMap();
    }

    private void GenerateMap()
    {
        for (int y = 0; y < mapHeight; y++)
        {
            for (int x = 0; x < mapWidth; x++)
            {
                float xPos = x * hexWidth + (y % 2 == 1 ? hexWidth / 2f : 0f); // ��������� ������� X
                float yPos = y * hexHeight; // ��������� ������� Y

                Vector3 hexPosition = new Vector3(xPos, yPos, 0f);

                GameObject hexGO = Instantiate(hexPrefab, hexPosition, Quaternion.identity);
                hexGO.transform.SetParent(transform); // ������������� ������������ ������

                Hex hex = hexGO.GetComponent<Hex>();
                hex.name = "Hex(" + x + "," + y + ")";
                hex.coordinates = new Vector2Int(x, y); // ������������� ���������� ���������
            }
        }
    }
        // Update is called once per frame
    void Update()
    {
        
    }
}
