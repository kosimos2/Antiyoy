using Photon.Pun;
using System.Collections;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using TMPro;
using Unity.VisualScripting;
using Unity.VisualScripting.Antlr3.Runtime;
using UnityEditor.Overlays;
using UnityEngine;
using UnityEngine.Tilemaps;
using UnityEngine.UIElements;

public class Hex : MonoBehaviour
{
    public string Team;
     
    public string Defence;
    public int Cost;    
    internal Vector2Int coordinates;
    
    public Tilemap tilemap;
    private PolygonCollider2D polygonCollider;
    private Grid grid;
    private Vector3Int position;
    public Unit Unit;

    
    

    
    // Start is called before the first frame update
    void Start()
    {
        
    }

    private Hex fromHex;
    public Hex()
    {
        fromHex = null; // »нициализируем значение пол€
        //„тобы сделать fromHex полем класса, вам следует объ€вить его как поле класса вместо локальной переменной в методе OnMouseDown.
        //“акже вам следует инициализировать это поле в конструкторе класса или в другом методе,
        //чтобы гарантировать, что оно будет инициализировано до первого вызова метода OnMouseDown.
    }
    private void OnMouseDown()
    {
        HexUnitManager unitManager = FindObjectOfType<HexUnitManager>();
        UnitMovement UnitMovement = FindObjectOfType<UnitMovement>();

        switch (UnitMovement.Score_Hex)
        {            
            case 0:
                unitManager.AddUnit(this);
                break;
            case 1:
                fromHex = this;
                Debug.Log(message: "Hex == " + fromHex);
                break;
            case 2:
                Debug.Log(message: "------------------" + fromHex + " + " + this);
                unitManager.MoveUnit(fromHex, this);
                UnitMovement.Score_Hex = 0;               
                break;
        }      
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
