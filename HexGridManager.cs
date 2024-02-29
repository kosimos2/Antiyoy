using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Tilemaps;

public class HexGridManager : MonoBehaviour
{
    public Tilemap hexTilemap;
    public HexUnitManager unitManager;
    public TileBase Void;
    public TileBase teamRed; 
    public TileBase teamBlue;
    public TileBase teamGreen;
    public TileBase teamTeal;
    public TileBase teamWhite;
    public TileBase teamYellow;

    private void Start()
    {
        // ѕолучаем все гексагоны на Tilemap       
    }

    void Update()
    {
        Hex[] hexes = FindObjectsOfType<Hex>();
        // ѕроходимс€ по каждому гексагону
        foreach (Hex hex in hexes)
        {
            // ѕолучаем позицию гексагона
            Vector3Int position = (Vector3Int)hex.coordinates;

            // ѕровер€ем переменную Team гексагона и мен€ем его спрайт в зависимости от команды
            if (hex.Team == "Void")
            {
                hexTilemap.SetTile(position, Void);
            }
            else if (hex.Team == "Red")
            {
                hexTilemap.SetTile(position, teamRed);
            }
            else if (hex.Team == "Green")
            {
                hexTilemap.SetTile(position, teamGreen);
            }
            else if (hex.Team == "Teal")
            {
                hexTilemap.SetTile(position, teamTeal);
            }
            else if (hex.Team == "White")
            {
                hexTilemap.SetTile(position, teamWhite);
            }
            else if (hex.Team == "Yellow")
            {
                hexTilemap.SetTile(position, teamYellow);
            }
            else if (hex.Team == "Red")
            {
                hexTilemap.SetTile(position, teamBlue);
            }
        }
    }
}
