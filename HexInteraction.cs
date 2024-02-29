using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HexInteraction : MonoBehaviour
{
    public HexUnitManager unitManager;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0)) // Проверяем, была ли нажата левая кнопка мыши
        {
            Vector2 mousePosition = Camera.main.ScreenToWorldPoint(Input.mousePosition); // Получаем позицию мыши в мировых координатах

            RaycastHit2D hit = Physics2D.Raycast(mousePosition, Vector2.zero); // Пускаем луч из позиции мыши

            if (hit.collider != null) // Проверяем, попал ли луч на коллайдер
            {
                GameObject hex = hit.collider.gameObject; // Получаем игровой объект гексагона              
                //Debug.Log(hex.name); // Выводим имя гексагона в консоль
            }
        }
    }
}
