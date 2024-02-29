using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class HexUnitManager : MonoBehaviour
{
    public GameObject unitPrefab; // префаб для создания юнитов
    public Sprite[] unitSprites; // Массив спрайтов для каждого Type
    private Dictionary<string, Sprite> spriteDict;

    public void AddUnit(Hex hex)
    {
        if (hex.Unit != null)
        {
            //hex.Unit.StartMovement();
            
        }
        else
        {


            // Создаем новый игровой объект Unit из префаба
            GameObject newUnit = Instantiate(unitPrefab, hex.transform.position, Quaternion.identity);
            newUnit.transform.SetParent(hex.transform);

            // Получаем компонент Unit из нового игрового объекта
            Unit unitComponent = newUnit.GetComponent<Unit>();

            // Устанавливаем атрибуты для нового юнита
            unitComponent.Type = "0";

            SpriteRenderer spriteRenderer = newUnit.GetComponent<SpriteRenderer>();
            if (spriteDict.ContainsKey(unitComponent.Type))
            {
                spriteRenderer.sprite = spriteDict[unitComponent.Type];
            }

            // Добавляем новый юнит в список или массив для хранения всех юнитов, если требуется

            // Дополнительные действия, связанные с созданием юнита
            hex.Unit = unitComponent;
            UnitMovement UnitMovement = FindObjectOfType<UnitMovement>();
            UnitMovement.Score_Hex = 0;
            Debug.Log(message: UnitMovement.Score_Hex + "HexUnitManager");

        }
    }

    public void MoveUnit(Hex fromHex, Hex toHex)
    {
        Debug.Log("MoveUnit");
        
        
        // Копируем данные удаленного Hex в новый Hex
        toHex.Unit = fromHex.Unit;
        toHex.Unit.transform.position = toHex.transform.position;
        toHex.Unit.transform.SetParent(toHex.transform);
        Debug.Log("12");
        // Очищаем данные удаленного Hex
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

        //if (Input.GetMouseButtonDown(0)) // Проверяем, была ли нажата левая кнопка мыши
        //{
        //    Vector2 mousePosition = Camera.main.ScreenToWorldPoint(Input.mousePosition); // Получаем позицию мыши в мировых координатах

        //    RaycastHit2D hit = Physics2D.Raycast(mousePosition, Vector2.zero); // Пускаем луч из позиции мыши

        //    if (hit.collider != null) // Проверяем, попал ли луч на коллайдер
        //    {
        //        GameObject hex = hit.collider.gameObject; // Получаем игровой объект гексагона              
                
        //    }
        //}

    }
}
