import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion, AnimatePresence } from "framer-motion";

const products = [
  // === ВСТАВЬ СЮДА ДАННЫЕ О ТОВАРАХ ===
  {
    id: 1,
    name: "Красные носки",
    image: "URL_КАРТИНКИ_НОСКОВ_1", // малое изображение
    largeImage: "URL_БОЛЬШОЙ_КАРТИНКИ_1",
    description: "Удобные красные носки из хлопка.",
  },
  {
    id: 2,
    name: "Синие носки",
    image: "URL_КАРТИНКИ_НОСКОВ_2",
    largeImage: "URL_БОЛЬШОЙ_КАРТИНКИ_2",
    description: "Яркие синие носки для любого случая.",
  },
  // Добавляй сколько нужно товаров по этому шаблону
];

export default function App() {
  const [selected, setSelected] = useState(null);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold text-center mb-4">SocksTeam — Магазин носков</h1>

      <div className="grid grid-cols-2 gap-4">
        {products.map((product) => (
          <motion.div whileHover={{ scale: 1.05 }} key={product.id}>
            <Card>
              <CardContent className="flex flex-col items-center p-2">
                <img src={product.image} alt={product.name} className="w-full h-32 object-cover rounded" />
                <Button className="mt-2 w-full" onClick={() => setSelected(product)}>
                  Подробнее
                </Button>
              </CardContent>
            </Card>
          </motion.div>
        ))}
      </div>

      <AnimatePresence>
        {selected && (
          <motion.div
            className="fixed inset-0 bg-black bg-opacity-60 flex items-center justify-center z-50"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          >
            <motion.div
              className="bg-white rounded-xl overflow-hidden max-w-md w-full"
              initial={{ scale: 0.8 }}
              animate={{ scale: 1 }}
              exit={{ scale: 0.8 }}
            >
              <img src={selected.largeImage} alt={selected.name} className="w-full h-64 object-cover" />
              <div className="p-4">
                <h2 className="text-xl font-semibold mb-2">{selected.name}</h2>
                <p className="mb-4">{selected.description}</p>
                {/* === ВСТАВЬ ССЫЛКУ НА СВОЙ ТЕЛЕГРАМ === */}
                <a
                  href="https://t.me/YOUR_TELEGRAM_USERNAME"
                  target="_blank"
                  className="inline-block bg-blue-600 text-white px-4 py-2 rounded text-center w-full"
                  rel="noopener noreferrer"
                >
                  Связаться с менеджером
                </a>
                <Button variant="outline" className="mt-2 w-full" onClick={() => setSelected(null)}>
                  Закрыть
                </Button>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
