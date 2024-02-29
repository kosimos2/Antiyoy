using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class HexUnitManager : MonoBehaviour
{
    public GameObject unitPrefab; // ������ ��� �������� ������
    public Sprite[] unitSprites; // ������ �������� ��� ������� Type
    private Dictionary<string, Sprite> spriteDict;

    public void AddUnit(Hex hex)
    {
        if (hex.Unit != null)
        {
            //hex.Unit.StartMovement();
            
        }
        else
        {


            // ������� ����� ������� ������ Unit �� �������
            GameObject newUnit = Instantiate(unitPrefab, hex.transform.position, Quaternion.identity);
            newUnit.transform.SetParent(hex.transform);

            // �������� ��������� Unit �� ������ �������� �������
            Unit unitComponent = newUnit.GetComponent<Unit>();

            // ������������� �������� ��� ������ �����
            unitComponent.Type = "0";

            SpriteRenderer spriteRenderer = newUnit.GetComponent<SpriteRenderer>();
            if (spriteDict.ContainsKey(unitComponent.Type))
            {
                spriteRenderer.sprite = spriteDict[unitComponent.Type];
            }

            // ��������� ����� ���� � ������ ��� ������ ��� �������� ���� ������, ���� ���������

            // �������������� ��������, ��������� � ��������� �����
            hex.Unit = unitComponent;
            UnitMovement UnitMovement = FindObjectOfType<UnitMovement>();
            UnitMovement.Score_Hex = 0;
            Debug.Log(message: UnitMovement.Score_Hex + "HexUnitManager");

        }
    }

    public void MoveUnit(Hex fromHex, Hex toHex)
    {
        Debug.Log("MoveUnit");
        
        
        // �������� ������ ���������� Hex � ����� Hex
        toHex.Unit = fromHex.Unit;
        toHex.Unit.transform.position = toHex.transform.position;
        toHex.Unit.transform.SetParent(toHex.transform);
        Debug.Log("12");
        // ������� ������ ���������� Hex
        fromHex.Unit = null;
        fromHex.Unit.IsDestroyed();
        Debug.Log("13");
        
    }
    public void RemoveUnit()
    {
        
    }
    
    // Start is called before the first frame update
    void Start()
    {
        spriteDict = new Dictionary<string, Sprite>();
        for (int i = 0; i < unitSprites.Length; i++)
        {
            spriteDict[i.ToString()] = unitSprites[i];
        }
    }

    // Update is called once per frame
    void Update()
    {

        //if (Input.GetMouseButtonDown(0)) // ���������, ���� �� ������ ����� ������ ����
        //{
        //    Vector2 mousePosition = Camera.main.ScreenToWorldPoint(Input.mousePosition); // �������� ������� ���� � ������� �����������

        //    RaycastHit2D hit = Physics2D.Raycast(mousePosition, Vector2.zero); // ������� ��� �� ������� ����

        //    if (hit.collider != null) // ���������, ����� �� ��� �� ���������
        //    {
        //        GameObject hex = hit.collider.gameObject; // �������� ������� ������ ���������              
                
        //    }
        //}

    }
}
