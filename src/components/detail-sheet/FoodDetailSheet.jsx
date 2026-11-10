import React, { useState } from "react";
import styles from "./FoodDetailSheet.module.css";
import { formatDistance, formatPriceRange, formatPrice } from "../map/mapGeoUtils";
import { KhueVanCacIcon } from "../icons/FoodIcons";

export default function FoodDetailSheet({
  place = null,
  dish = null,
  onClose,
  onSelectPlace,
  onSelectDish,
  categoryMeta = {},
}) {
  const [activeTab, setActiveTab] = useState("overview");

  if (!place && !dish) return null;

  const isPlaceMode = Boolean(place);
  const isVanMieu = place?.isCenterLandmark;

  // Van Mieu Center Landmark Special Card
  if (isVanMieu) {
    return (
      <div className={styles.sheetOverlay} onClick={onClose}>
        <div className={styles.sheetContainer} onClick={(e) => e.stopPropagation()}>
          <div className={styles.headerImageWrapper}>
            <img
              src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Hanoi_Temple_of_Literature_01.jpg/1200px-Hanoi_Temple_of_Literature_01.jpg"
              alt="Văn Miếu Quốc Tử Giám"
              className={styles.headerImage}
            />
            <button className={styles.closeBtn} onClick={onClose} title="Đóng">
              ✕
            </button>
            <div className={styles.imageOverlay}>
              <div className={styles.headerTagRow}>
                <span className={styles.heritageTag}>🏛️ Di Tích Quốc Gia Đặc Biệt</span>
                <span className={styles.sourceTag} title="Nguồn ảnh: Wikimedia Commons (CC BY-SA)">
                  📷 Wikimedia Commons (Jean-Pierre Dalbéra)
                </span>
              </div>
              <h2 className={styles.sheetTitle}>Văn Miếu – Quốc Tử Giám</h2>
              <p className={styles.sheetSubtitle}>Tâm điểm khảo sát ẩm thực tinh hoa Hà Nội</p>
            </div>
          </div>

          <div className={styles.sheetBody}>
            <div className={styles.quickInfoGrid}>
              <div className={styles.infoCard}>
                <span className={styles.infoNumber}>2.0 km</span>
                <span className={styles.infoLabel}>Bán kính khảo sát</span>
              </div>
              <div className={styles.infoCard}>
                <span className={styles.infoNumber}>70</span>
                <span className={styles.infoLabel}>Quán ăn đặc sản</span>
              </div>
              <div className={styles.infoCard}>
                <span className={styles.infoNumber}>50</span>
                <span className={styles.infoLabel}>Món ăn truyền thống</span>
              </div>
              <div className={styles.infoCard}>
                <span className={styles.infoNumber}>308</span>
                <span className={styles.infoLabel}>Nguyên liệu định danh</span>
              </div>
            </div>

            <div className={styles.section}>
              <h3 className={styles.sectionTitle}>Thông tin tọa độ & Địa chỉ</h3>
              <p className={styles.textParagraph}>
                <strong>Địa chỉ:</strong> 58 Quốc Tử Giám, Phường Văn Miếu, Quận Đống Đa, Hà Nội.
              </p>
              <p className={styles.textParagraph}>
                <strong>Tọa độ GPS:</strong> 21.02879° N, 105.835953° E (Tâm điểm tính khoảng cách của toàn bộ hệ thống).
              </p>
              <p className={styles.textParagraph}>
                Vùng bán kính 2km bao phủ các con phố ẩm thực trứ danh của Hà Nội: Nguyễn Khuyến, Văn Miếu, Tôn Đức Thắng, Phan Bội Châu, Phủ Doãn, Lý Quốc Sư, Hàng Nón, Bát Đàn, Cửa Nam.
              </p>
            </div>

            <div className={styles.actionButtons}>
              <a
                href="https://www.google.com/maps/search/?api=1&query=Văn+Miếu+Quốc+Tử+Giám"
                target="_blank"
                rel="noreferrer"
                className={styles.primaryBtn}
              >
                🗺️ Mở trên Google Maps
              </a>
            </div>
          </div>
        </div>
      </div>
    );
  }

  // PLACE MODE
  if (isPlaceMode) {
    const catMeta = categoryMeta[place.primary_category] || {};
    const dishesServed = place.dishes || [];

    return (
      <div className={styles.sheetOverlay} onClick={onClose}>
        <div className={styles.sheetContainer} onClick={(e) => e.stopPropagation()}>
          <div className={styles.headerImageWrapper}>
            <img
              src={place.image_url}
              alt={place.name}
              className={styles.headerImage}
              onError={(e) => {
                e.target.src = place.online_image_url || "/images/dishes/DISH_001.jpg";
              }}
            />
            <button className={styles.closeBtn} onClick={onClose} title="Đóng">
              ✕
            </button>
            <div className={styles.imageOverlay}>
              <div className={styles.headerTagRow}>
                <span className={styles.heritageTag}>
                  {catMeta.icon || "📍"} {catMeta.label || "Quán ăn"}
                </span>
                {place.image_source && (
                  <span className={styles.sourceTag} title={`Nguồn ảnh: ${place.image_source}`}>
                    📷 {place.image_source}
                  </span>
                )}
              </div>
              <h2 className={styles.sheetTitle}>{place.name}</h2>
              {place.branch_name && <p className={styles.sheetBranch}>{place.branch_name}</p>}
              <div className={styles.headerMetaRow}>
                <span className={styles.headerRating}>★ {place.rating} ({place.review_count} đánh giá)</span>
                <span className={styles.headerDistance}>🧭 Cách Văn Miếu {formatDistance(place.distance_m)}</span>
              </div>
            </div>
          </div>

          {/* Navigation Tabs */}
          <div className={styles.tabNav}>
            <button
              className={`${styles.tabBtn} ${activeTab === "overview" ? styles.tabActive : ""}`}
              onClick={() => setActiveTab("overview")}
            >
              Tổng quan
            </button>
            <button
              className={`${styles.tabBtn} ${activeTab === "menu" ? styles.tabActive : ""}`}
              onClick={() => setActiveTab("menu")}
            >
              Thực đơn ({dishesServed.length})
            </button>
          </div>

          <div className={styles.sheetBody}>
            {activeTab === "overview" && (
              <>
                <div className={styles.metaBox}>
                  <div className={styles.metaRow}>
                    <span className={styles.metaIcon}>📍</span>
                    <div>
                      <strong>Địa chỉ:</strong>
                      <p className={styles.metaVal}>{place.address}</p>
                    </div>
                  </div>

                  <div className={styles.metaRow}>
                    <span className={styles.metaIcon}>🕒</span>
                    <div>
                      <strong>Giờ mở cửa:</strong>
                      <p className={styles.metaVal}>{place.opening_hours || "07:00 - 21:00"}</p>
                    </div>
                  </div>

                  <div className={styles.metaRow}>
                    <span className={styles.metaIcon}>💰</span>
                    <div>
                      <strong>Khoảng giá tham khảo:</strong>
                      <p className={styles.metaVal}>
                        {formatPriceRange(place.price_min_vnd, place.price_max_vnd)}
                      </p>
                    </div>
                  </div>

                  <div className={styles.metaRow}>
                    <span className={styles.metaIcon}>🧭</span>
                    <div>
                      <strong>Khoảng cách từ Văn Miếu:</strong>
                      <p className={styles.metaVal}>
                        {formatDistance(place.distance_m)} (đường chim bay)
                      </p>
                    </div>
                  </div>
                </div>

                <div className={styles.actionButtons}>
                  <a
                    href={`https://www.google.com/maps/dir/?api=1&origin=21.02879,105.835953&destination=${place.lat},${place.lng}`}
                    target="_blank"
                    rel="noreferrer"
                    className={styles.primaryBtn}
                  >
                    🧭 Chỉ đường từ Văn Miếu
                  </a>
                </div>

                <div className={styles.section}>
                  <h3 className={styles.sectionTitle}>Các món đặc sản phục vụ</h3>
                  <div className={styles.miniDishGrid}>
                    {dishesServed.map((d, idx) => (
                      <div
                        key={idx}
                        className={styles.miniDishCard}
                        onClick={() => {
                          if (onSelectDish) onSelectDish({ dish_id: d.dish_id });
                        }}
                      >
                        <div className={styles.miniDishLeft}>
                          {d.image_url && (
                            <img
                              src={d.image_url}
                              alt={d.dish_name_vi}
                              className={styles.miniDishThumb}
                              loading="lazy"
                              onError={(e) => {
                                e.target.src = d.online_image_url || "/images/dishes/DISH_001.jpg";
                              }}
                            />
                          )}
                          <div>
                            <span className={styles.miniDishName}>{d.dish_name_vi}</span>
                            {d.variant && <span className={styles.miniDishVariant}>({d.variant})</span>}
                            {d.image_source && (
                              <span className={styles.miniDishSource}>📷 {d.image_source}</span>
                            )}
                          </div>
                        </div>
                        <span className={styles.miniDishPrice}>{formatPrice(d.price_min_vnd)}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </>
            )}

            {activeTab === "menu" && (
              <div className={styles.section}>
                <h3 className={styles.sectionTitle}>Thực đơn món ăn tại quán</h3>
                <div className={styles.menuList}>
                  {dishesServed.map((item, idx) => (
                    <div key={idx} className={styles.menuItem}>
                      <div className={styles.menuItemRow}>
                        {item.image_url && (
                          <img
                            src={item.image_url}
                            alt={item.dish_name_vi}
                            className={styles.menuItemThumb}
                            loading="lazy"
                            onError={(e) => {
                              e.target.src = item.online_image_url || "/images/dishes/DISH_001.jpg";
                            }}
                          />
                        )}
                        <div className={styles.menuItemContent}>
                          <div className={styles.menuItemHeader}>
                            <h4 className={styles.menuItemName}>{item.menu_item_name_vi || item.dish_name_vi}</h4>
                            <span className={styles.menuItemPrice}>
                              {formatPriceRange(item.price_min_vnd, item.price_max_vnd)}
                            </span>
                          </div>
                          {item.menu_item_name_en && (
                            <p className={styles.menuItemEn}>{item.menu_item_name_en}</p>
                          )}
                          <div className={styles.menuItemDetails}>
                            {item.variant && <span className={styles.pillTag}>Biến thể: {item.variant}</span>}
                            {item.portion && <span className={styles.pillTag}>Khẩu phần: {item.portion}</span>}
                            {item.image_source && (
                              <span className={styles.sourcePill} title="Nguồn ảnh thực tế tại quán">
                                📷 {item.image_source}
                              </span>
                            )}
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    );
  }

  // DISH MODE
  const catMeta = categoryMeta[dish.category] || {};
  const servingPlaces = dish.serving_places || [];
  const ingredients = dish.ingredients || [];

  // Group ingredients by group
  const groupedIngredients = {};
  ingredients.forEach((ing) => {
    const grp = ing.group || "Khác";
    if (!groupedIngredients[grp]) groupedIngredients[grp] = [];
    groupedIngredients[grp].push(ing);
  });

  return (
    <div className={styles.sheetOverlay} onClick={onClose}>
      <div className={styles.sheetContainer} onClick={(e) => e.stopPropagation()}>
        <div className={styles.headerImageWrapper}>
          <img
            src={dish.image_url}
            alt={dish.name_vi}
            className={styles.headerImage}
            onError={(e) => {
              e.target.src = dish.online_image_url || "/images/dishes/DISH_001.jpg";
            }}
          />
          <button className={styles.closeBtn} onClick={onClose} title="Đóng">
            ✕
          </button>
          <div className={styles.imageOverlay}>
            <div className={styles.headerTagRow}>
              <span className={styles.heritageTag}>
                {catMeta.icon || "🍲"} {catMeta.label || "Món ăn"}
              </span>
              {dish.image_source && (
                <span className={styles.sourceTag} title={`Nguồn ảnh: ${dish.image_source}`}>
                  📷 {dish.image_source}
                </span>
              )}
            </div>
            <h2 className={styles.sheetTitle}>{dish.name_vi}</h2>
            {dish.name_en && <p className={styles.sheetBranch}>{dish.name_en}</p>}
            {dish.taste_profile && dish.taste_profile.length > 0 && (
              <div className={styles.tastePills}>
                {dish.taste_profile.map((t, idx) => (
                  <span key={idx} className={styles.tastePill}>
                    #{t}
                  </span>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Tab Navigation */}
        <div className={styles.tabNav}>
          <button
            className={`${styles.tabBtn} ${activeTab === "overview" ? styles.tabActive : ""}`}
            onClick={() => setActiveTab("overview")}
          >
            Tổng quan
          </button>
          <button
            className={`${styles.tabBtn} ${activeTab === "places" ? styles.tabActive : ""}`}
            onClick={() => setActiveTab("places")}
          >
            Quán phục vụ ({servingPlaces.length})
          </button>
          <button
            className={`${styles.tabBtn} ${activeTab === "ingredients" ? styles.tabActive : ""}`}
            onClick={() => setActiveTab("ingredients")}
          >
            Nguyên liệu ({ingredients.length})
          </button>
          <button
            className={`${styles.tabBtn} ${activeTab === "how_to_eat" ? styles.tabActive : ""}`}
            onClick={() => setActiveTab("how_to_eat")}
          >
            Cách ăn & Gọi món
          </button>
        </div>

        <div className={styles.sheetBody}>
          {activeTab === "overview" && (
            <>
              <div className={styles.section}>
                <h3 className={styles.sectionTitle}>Giới thiệu món ăn</h3>
                <p className={styles.textParagraph}>
                  {dish.description_vi || dish.short_description_vi || "Món ăn truyền thống đậm đà phong vị đất Kinh Kỳ."}
                </p>
                {dish.aliases && dish.aliases.length > 0 && (
                  <p className={styles.aliasText}>
                    <strong>Tên gọi khác:</strong> {dish.aliases.join(", ")}
                  </p>
                )}
              </div>

              {dish.meal_times && dish.meal_times.length > 0 && (
                <div className={styles.section}>
                  <h3 className={styles.sectionTitle}>Thời điểm thưởng thức phù hợp</h3>
                  <div className={styles.mealTimeBadges}>
                    {dish.meal_times.map((mt, idx) => (
                      <span key={idx} className={styles.mealBadge}>
                        ⏰ {mt}
                      </span>
                    ))}
                  </div>
                </div>
              )}

              {dish.allergens_by_recipe && dish.allergens_by_recipe.length > 0 && (
                <div className={styles.warningBox}>
                  <strong>⚠️ Lưu ý thành phần dị ứng:</strong> {dish.allergens_by_recipe.join(", ")}
                </div>
              )}

              <div className={styles.section}>
                <h3 className={styles.sectionTitle}>
                  Các quán gần Văn Miếu phục vụ ({servingPlaces.length})
                </h3>
                <div className={styles.placesList}>
                  {servingPlaces.map((p) => (
                    <div
                      key={p.place_id}
                      className={styles.servingPlaceCard}
                      onClick={() => onSelectPlace && onSelectPlace(p)}
                    >
                      <div className={styles.placeCardHeader}>
                        <span className={styles.servingPlaceName}>{p.name}</span>
                        <span className={styles.servingPlaceDist}>
                          🧭 {formatDistance(p.distance_m)}
                        </span>
                      </div>
                      <p className={styles.servingPlaceAddr}>{p.address}</p>
                    </div>
                  ))}
                </div>
              </div>
            </>
          )}

          {activeTab === "places" && (
            <div className={styles.section}>
              <h3 className={styles.sectionTitle}>Danh sách quán ăn phục vụ gần Văn Miếu</h3>
              <div className={styles.placesList}>
                {servingPlaces.map((p) => (
                  <div
                    key={p.place_id}
                    className={styles.servingPlaceCard}
                    onClick={() => onSelectPlace && onSelectPlace(p)}
                  >
                    <div className={styles.placeCardHeader}>
                      <span className={styles.servingPlaceName}>{p.name}</span>
                      <span className={styles.servingPlaceDist}>
                        🧭 {formatDistance(p.distance_m)}
                      </span>
                    </div>
                    <p className={styles.servingPlaceAddr}>{p.address}</p>
                    <div className={styles.placeCardFooter}>
                      <span>★ {p.rating}</span>
                      <span>Giờ mở cửa: {p.opening_hours || "07:00 - 21:00"}</span>
                      <span className={styles.viewOnMapText}>Xem trên bản đồ →</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {activeTab === "ingredients" && (
            <div className={styles.section}>
              <h3 className={styles.sectionTitle}>Thành phần nguyên liệu ({ingredients.length})</h3>
              {Object.entries(groupedIngredients).map(([grp, items]) => (
                <div key={grp} className={styles.ingredientGroup}>
                  <h4 className={styles.ingredientGroupTitle}>{grp.toUpperCase()}</h4>
                  <div className={styles.ingredientGrid}>
                    {items.map((ing, idx) => (
                      <div key={idx} className={styles.ingredientItem}>
                        <span className={styles.ingName}>{ing.name_vi}</span>
                        {ing.quantity_raw && (
                          <span className={styles.ingQty}>{ing.quantity_raw}</span>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          )}

          {activeTab === "how_to_eat" && (
            <>
              {dish.how_to_eat_vi && (
                <div className={styles.section}>
                  <h3 className={styles.sectionTitle}>Cách thưởng thức chuẩn vị Hà Nội</h3>
                  <div className={styles.tipBox}>
                    <p className={styles.tipText}>{dish.how_to_eat_vi}</p>
                  </div>
                </div>
              )}

              {dish.ordering_phrase_vi && (
                <div className={styles.section}>
                  <h3 className={styles.sectionTitle}>Cách gọi món sành điệu</h3>
                  <div className={styles.orderingBox}>
                    <p className={styles.orderingPhrase}>"{dish.ordering_phrase_vi}"</p>
                  </div>
                </div>
              )}

              {dish.recipe_video_embed_url && (
                <div className={styles.section}>
                  <h3 className={styles.sectionTitle}>Video hướng dẫn chế biến</h3>
                  <div className={styles.videoEmbed}>
                    <iframe
                      src={dish.recipe_video_embed_url}
                      title={dish.name_vi}
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowFullScreen
                    />
                  </div>
                  {dish.recipe_video_creator && (
                    <p className={styles.creatorCredit}>
                      Nguồn video: {dish.recipe_video_creator}
                    </p>
                  )}
                </div>
              )}
            </>
          )}
        </div>
      </div>
    </div>
  );
}

