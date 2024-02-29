using UnityEngine;

public class UnitMovement : MonoBehaviour
{
    public static int Score_Hex;
    // Start is called before the first frame update
    void Start()
    {
        Score_Hex = 0;
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
                Hex hex = hit.collider.GetComponent<Hex>();
                Debug.Log(message: "UnitMovement == "+ hex.Unit + " + " + Score_Hex);

                if (hex.Unit == null && Score_Hex == 0)
                {
                    Score_Hex = 0;
                }
                else if (hex.Unit != null && Score_Hex == 0)
                {
                    Score_Hex = 1;                  
                }
                else if (hex.Unit == null && Score_Hex == 1)
                {
                    Score_Hex = 2;
                }
                else if (hex.Unit != null && Score_Hex == 2)
                {
                    Score_Hex = 0;
                }
            }
        }

    }
    


}
